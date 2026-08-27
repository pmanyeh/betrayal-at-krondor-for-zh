"""
Unit tests for the BOK book extractor/packer round-trip (Phase 7).

Verifies:
1. A synthetic minimal BOK fixture round-trips byte-identically.
2. The packer recomputes the page-offset table and file-size header when a
   localized text stream changes length, and the result re-parses cleanly.
3. Every real Cxx.BOK in krondor.001 round-trips byte-identically.
"""

import hashlib
import struct
import unittest
from pathlib import Path

from tools.text.bok_extract import extract_bok_data
from tools.text.bok_layout import append_overflow_pages, raise_line_height
from tools.text.bok_pack import pack_bok_data, validate_bok_data


def _synthetic_bok() -> bytes:
    """Two pages: page 0 carries a tagged text stream, page 1 is an overflow target."""
    def page(rect, nav, reserved_rects, images, stream):
        hdr = struct.pack("<hhhh9H", *rect, *nav) + b"\x00" * 30
        body = b"".join(struct.pack("<hhhh", *r) for r in reserved_rects)
        body += b"".join(struct.pack("<hhHH", *im) for im in images)
        return hdr + body + stream

    layout = b"\xF1" + b"\x0a\x00\x0a\x00\x0f\x00\x04\x00\x1e\x00\x00\x00\x00\x00\x03\x00"
    style = b"\xF4" + b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00"
    stream0 = layout + style + b"Hello book world." + layout + style + b"Second paragraph." + b"\xF0"
    p0 = page((40, 80, 554, 240), (1, 1, 0xFFFF, 2, 2, 0, 1, 1, 1),
              [(30, 10, 102, 98)], [(30, 14, 0, 0)], stream0)
    p1 = page((40, 35, 554, 285), (2, 2, 1, 0xFFFE, 0xFFFF, 0, 0, 0, 1), [], [], b"\xF0")

    table_size = 2 + 2 * 4
    blob = struct.pack("<h", 2) + struct.pack("<I", table_size) + struct.pack("<I", table_size + len(p0)) + p0 + p1
    return struct.pack("<I", len(blob)) + blob


class TestBokRoundTrip(unittest.TestCase):
    def test_synthetic_roundtrip(self):
        raw = _synthetic_bok()
        extracted = extract_bok_data(raw)
        self.assertEqual(extracted["page_count"], 2)
        runs = [it for pg in extracted["pages"] for it in pg["stream"] if it["kind"] == "text"]
        self.assertEqual([r["text"] for r in runs], ["Hello book world.", "Second paragraph."])
        self.assertEqual(pack_bok_data(extracted), raw)

    def test_length_change_recomputes_offsets(self):
        extracted = extract_bok_data(_synthetic_bok())
        for pg in extracted["pages"]:
            for it in pg["stream"]:
                if it["kind"] == "text":
                    it["text"] = it["text"] + "\x81\x40" * 32  # simulate CJK byte expansion

        packed = pack_bok_data(extracted)
        validate_bok_data(packed, "synthetic-lengthened")
        reparsed = extract_bok_data(packed)

        n = reparsed["page_count"]
        offsets = [struct.unpack_from("<I", packed, 6 + i * 4)[0] for i in range(n)]
        self.assertEqual(offsets, sorted(offsets))
        self.assertEqual(offsets[0], 2 + 4 * n)
        self.assertEqual(struct.unpack_from("<I", packed, 0)[0], len(packed) - 4)

        for a, b in zip(extracted["pages"], reparsed["pages"]):
            self.assertEqual(a["wPageNumber"], b["wPageNumber"])
            self.assertEqual(a["wNextPageNumber"], b["wNextPageNumber"])
            self.assertEqual(
                [it.get("text") for it in a["stream"]],
                [it.get("text") for it in b["stream"]],
            )

    def test_raise_line_height(self):
        extracted = extract_bok_data(_synthetic_bok())
        changed = raise_line_height(extracted, target=18)
        self.assertEqual(changed, 2)  # both paragraphs' layout blocks
        for pg in extracted["pages"]:
            for it in pg["stream"]:
                if it["kind"] == "layout":
                    lh = int.from_bytes(bytes.fromhex(it["hex"])[4:6], "little", signed=True)
                    self.assertEqual(lh, 18)
        # idempotent / never lowers
        self.assertEqual(raise_line_height(extracted, target=15), 0)
        packed = pack_bok_data(extracted)
        validate_bok_data(packed, "line-height")

    def test_append_overflow_pages_rechains_tail(self):
        extracted = extract_bok_data(_synthetic_bok())
        tail_before = extracted["pages"][-1]
        orig_next, orig_ptr = tail_before["wNextPageNumber"], tail_before["wPagePointer"]
        added = append_overflow_pages(extracted, count=2)
        self.assertEqual(added, 2)
        self.assertEqual(extracted["page_count"], 4)

        pages = extracted["pages"]
        # old tail now points at the first spare, next == ptr (engine's terminate check)
        old_tail = pages[1]
        self.assertEqual(old_tail["wNextPageNumber"], old_tail["wPagePointer"])
        self.assertEqual(old_tail["wNextPageNumber"], pages[2]["wPageNumber"])
        # spares are blank and linked; the last one carries the original terminator
        for sp in pages[2:]:
            self.assertEqual([i["kind"] for i in sp["stream"]], ["end"])
            self.assertEqual(sp["wImageCount"], 0)
        self.assertEqual(pages[2]["wNextPageNumber"], pages[3]["wPageNumber"])
        self.assertEqual(pages[3]["wNextPageNumber"], orig_next)
        self.assertEqual(pages[3]["wPagePointer"], orig_ptr)

        validate_bok_data(pack_bok_data(extracted), "overflow-pages")

    def test_append_overflow_pages_skips_nonstandard_tail(self):
        extracted = extract_bok_data(_synthetic_bok())
        extracted["pages"][-1]["wNextPageNumber"] = 99  # points nowhere, not a terminator
        self.assertEqual(append_overflow_pages(extracted, count=2), 0)
        self.assertEqual(extracted["page_count"], 2)

    def test_real_game_bok_roundtrips(self):
        rmf_path = Path(r"d:\git\betrayal-at-krondor-for-zh\betrayal-at-krondor\krondor.rmf")
        arc_path = Path(r"d:\git\betrayal-at-krondor-for-zh\betrayal-at-krondor\krondor.001")
        if not rmf_path.exists() or not arc_path.exists():
            self.skipTest("Game data files not present, skipping real BOK round-trip test")

        rmf_data = rmf_path.read_bytes()
        (count,) = struct.unpack_from("<H", rmf_data, 19)
        tested = 0
        with arc_path.open("rb") as f:
            for i in range(count):
                _, off = struct.unpack_from("<II", rmf_data, 21 + i * 8)
                f.seek(off)
                entry_hdr = f.read(17)
                name = entry_hdr[:13].split(b"\0", 1)[0].decode("ascii")
                (size,) = struct.unpack_from("<I", entry_hdr, 13)
                if name.upper().startswith("C") and name.upper().endswith(".BOK"):
                    original = f.read(size)
                    repacked = pack_bok_data(extract_bok_data(original))
                    self.assertEqual(
                        hashlib.sha256(original).hexdigest(),
                        hashlib.sha256(repacked).hexdigest(),
                        f"{name} did not round-trip byte-identically",
                    )
                    tested += 1
        self.assertEqual(tested, 22)


if __name__ == "__main__":
    unittest.main()
