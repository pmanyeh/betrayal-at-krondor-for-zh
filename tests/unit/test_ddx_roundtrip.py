"""
Unit Tests for DDX Extractor and Packer Round-Trip (Phase 2)
Verifies:
1. Synthetic minimal DDX fixture round-trip.
2. Real DDX files from game resource (krondor.001) round-trip:
   DDX -> extract to JSON -> pack to DDX -> Byte-Identical match (SHA-256).
"""

import hashlib
import struct
import unittest
from pathlib import Path

from tools.text.ddx_extract import extract_ddx_data
from tools.text.ddx_pack import pack_ddx_data


class TestDdxRoundTrip(unittest.TestCase):
    def test_synthetic_roundtrip(self):
        """Build a synthetic DDX binary with keyed and child records, verify exact byte round-trip."""
        # 2 records: Rec 1 at off 18, Rec 2 (child) at off 18 + len(rec1)
        choice1 = struct.pack("<HHHHH", 100, 1, 2, 49, 4)
        opcode1 = struct.pack("<HHHHH", 200, 5, 6, 7, 8)
        body1 = b"Hello World\x00"
        rec1_hdr = struct.pack("<BHHBBH", 1, 2, 0x200, 1, 1, len(body1))
        rec1 = rec1_hdr + choice1 + opcode1 + body1

        body2 = b"#Title#\nSecond line.\x00"
        rec2_hdr = struct.pack("<BHHBBH", 0, 0, 0, 0, 0, len(body2))
        rec2 = rec2_hdr + body2

        synthetic_ddx = (
            struct.pack("<H", 1)  # 1 keyed directory entry
            + struct.pack("<II", 100001, 10)  # Directory: 2 + 8 = 10 bytes
            + rec1
            + rec2
        )

        extracted = extract_ddx_data(synthetic_ddx)
        self.assertEqual(extracted["total_records"], 2)
        self.assertEqual(len(extracted["dir_entries"]), 1)
        self.assertEqual(extracted["records"][0]["node_id"], 100001)
        self.assertIsNone(extracted["records"][1]["node_id"])

        repacked = pack_ddx_data(extracted)
        self.assertEqual(repacked, synthetic_ddx)

    def test_real_game_ddx_roundtrips(self):
        """Extract all DDX files from krondor.001 and verify 100% byte-identical round-trip."""
        rmf_path = Path(r"d:\git\betrayal-at-krondor-for-zh\betrayal-at-krondor\krondor.rmf")
        arc_path = Path(r"d:\git\betrayal-at-krondor-for-zh\betrayal-at-krondor\krondor.001")

        if not rmf_path.exists() or not arc_path.exists():
            self.skipTest("Game data files not present, skipping real DDX round-trip test")

        rmf_data = rmf_path.read_bytes()
        (count,) = struct.unpack_from("<H", rmf_data, 19)
        table = 21

        tested_files = 0
        with arc_path.open("rb") as f:
            for i in range(count):
                hkey, off = struct.unpack_from("<II", rmf_data, table + i * 8)
                f.seek(off)
                entry_hdr = f.read(17)
                name = entry_hdr[:13].split(b"\0", 1)[0].decode("ascii")
                (size,) = struct.unpack_from("<I", entry_hdr, 13)

                if name.upper().endswith(".DDX") and size > 2:
                    original_ddx = f.read(size)
                    extracted = extract_ddx_data(original_ddx)
                    repacked = pack_ddx_data(extracted)

                    orig_sha = hashlib.sha256(original_ddx).hexdigest()
                    repack_sha = hashlib.sha256(repacked).hexdigest()

                    self.assertEqual(
                        repacked,
                        original_ddx,
                        f"Round-trip byte mismatch for {name}: {repack_sha} vs {orig_sha}",
                    )
                    tested_files += 1

        print(f"Verified byte-identical round-trip for {tested_files} game DDX files.")
        self.assertEqual(tested_files, 29)


if __name__ == "__main__":
    unittest.main()
