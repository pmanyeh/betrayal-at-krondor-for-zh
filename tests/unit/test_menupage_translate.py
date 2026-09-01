import argparse
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.text import menupage_translate as mp


def make_menupage(title, entries):
    """entries: list of (label, primary, alt) with None for absent slots."""
    pool = bytearray()
    interned = {}

    def off(s):
        if s is None:
            return 0xFFFF
        key = s.encode("latin1")
        if key not in interned:
            interned[key] = len(pool)
            pool.extend(key + b"\0")
        return interned[key]

    hdr = bytearray(28)
    struct.pack_into("<H", hdr, mp.TITLE_OFF, off(title))
    body = bytearray(struct.pack("<H", len(entries)))
    for label, primary, alt in entries:
        rec = bytearray(mp.ENTRY_SIZE)
        struct.pack_into("<H", rec, 19, off(label))
        struct.pack_into("<H", rec, 21, off(primary))
        struct.pack_into("<H", rec, 23, off(alt))
        body.extend(rec)
    return bytes(hdr) + bytes(body) + struct.pack("<H", len(pool)) + bytes(pool)


ENTRIES = [(None, "Save", None), (None, "Cancel", None), (None, None, "East of Zun")]


class TestMenupageCodec(unittest.TestCase):
    def test_decode(self):
        page = mp.decode_menupage(make_menupage("Options", ENTRIES))
        self.assertEqual(page["title"], "Options")
        self.assertEqual([e["primary"] for e in page["entries"]], ["Save", "Cancel", None])
        self.assertEqual(page["entries"][2]["alt"], "East of Zun")

    def test_blobsize_mismatch_rejected(self):
        raw = bytearray(make_menupage(None, ENTRIES))
        blob_off = 30 + len(ENTRIES) * mp.ENTRY_SIZE
        struct.pack_into("<H", raw, blob_off, 999)
        with self.assertRaises(ValueError):
            mp.decode_menupage(bytes(raw))


class TestMenupageBuild(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.pris = self.root / "pris"
        self.out = self.root / "out"
        self.pris.mkdir()
        (self.pris / "REQ_OPT1.DAT").write_bytes(make_menupage(None, ENTRIES))
        (self.pris / "REQ_DBUG.DAT").write_bytes(make_menupage(None, [(None, "Done", None)]))

    def _build(self, entries, mapping, injected_entries=None):
        cat = self.root / "MENUPAGE.json"
        mpath = self.root / "map.json"
        cat.write_text(json.dumps({"entries": entries,
                                   "injected_entries": injected_entries or []},
                                  ensure_ascii=False), encoding="utf-8")
        mpath.write_text(json.dumps({"char_to_id": mapping}), encoding="utf-8")
        mp.cmd_build(argparse.Namespace(
            pristine_dir=str(self.pris), json_path=str(cat), out_dir=str(self.out),
            mapping=str(mpath)))

    def test_untranslated_build_is_byte_identical(self):
        self._build([], {})
        for name in ("REQ_OPT1.DAT", "REQ_DBUG.DAT"):
            self.assertEqual((self.out / name).read_bytes(), (self.pris / name).read_bytes())

    def test_translation_repoints_and_keeps_other_files_identical(self):
        mapping = {"儲": 0, "存": 1}
        self._build([{"id": "REQ_OPT1.DAT#0#primary", "file": "REQ_OPT1.DAT", "entry": 0,
                      "slot": "primary", "source": "Save", "translation": "儲存",
                      "status": "translated"}], mapping)
        page = mp.decode_menupage((self.out / "REQ_OPT1.DAT").read_bytes())
        self.assertEqual(page["entries"][0]["primary"],
                         mp.encode_string("儲存", mapping).decode("latin1"))
        self.assertEqual(page["entries"][1]["primary"], "Cancel")  # untouched
        # unrelated file untouched
        self.assertEqual((self.out / "REQ_DBUG.DAT").read_bytes(),
                         (self.pris / "REQ_DBUG.DAT").read_bytes())

    def test_source_drift_falls_back(self):
        self._build([{"id": "REQ_OPT1.DAT#0#primary", "file": "REQ_OPT1.DAT", "entry": 0,
                      "slot": "primary", "source": "Store", "translation": "儲",
                      "status": "translated"}], {"儲": 0})
        page = mp.decode_menupage((self.out / "REQ_OPT1.DAT").read_bytes())
        self.assertEqual(page["entries"][0]["primary"], "Save")

    def test_injected_button_clones_style_and_sets_action_rect_and_text(self):
        mapping = {"啟": 0, "動": 1}
        self._build([], mapping, [{
            "file": "REQ_OPT1.DAT", "insert_at": 1, "copy_entry": 0,
            "action_id": 0x83, "rect": [40, 130, 240, 20], "primary": "啟動",
        }])
        raw = (self.out / "REQ_OPT1.DAT").read_bytes()
        page = mp.decode_menupage(raw)
        self.assertEqual(page["count"], 4)
        self.assertEqual(page["entries"][1]["primary"],
                         mp.encode_string("啟動", mapping).decode("latin1"))
        rec = raw[mp.HEADER_SIZE + 2 + mp.ENTRY_SIZE:
                  mp.HEADER_SIZE + 2 + 2 * mp.ENTRY_SIZE]
        self.assertEqual(struct.unpack_from("<H", rec, 2)[0], 0x83)
        self.assertEqual(struct.unpack_from("<hhhh", rec, 11), (40, 130, 240, 20))


if __name__ == "__main__":
    unittest.main()
