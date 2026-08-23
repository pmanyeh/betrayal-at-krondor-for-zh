"""
Unit test for the OBJINFO.DAT item-name translation pipeline.

Regression test for a real bug: build() wrote the post-translation
"reset to single-line" value at ItemRecord offset 32 (immediately after
the 32-byte pName), which is actually the wFlags field -- wName_split_off
is the NEXT u16, at offset 34. Every translated item silently lost its
wFlags (durability%/stack-count display, equip slot, etc.) even though
the translation JSON, tokens, and encoding were all otherwise correct.
"""

import argparse
import json
import struct
import unittest
from pathlib import Path

from tools.text import objinfo_translate as ot


class TestObjinfoTranslate(unittest.TestCase):
    def _make_pristine(self, name: bytes, wflags: int, split_off: int) -> bytes:
        record = bytearray(ot.RECORD_SIZE)
        record[: len(name)] = name
        struct.pack_into("<H", record, 32, wflags)
        struct.pack_into("<H", record, 34, split_off)
        blob = bytearray()
        for i in range(ot.RECORD_COUNT):
            blob += record if i == 1 else bytearray(ot.RECORD_SIZE)
        blob += bytes(ot.TRAILER_SIZE)
        self.assertEqual(len(blob), ot.EXPECTED_FILE_SIZE)
        return bytes(blob)

    def test_build_preserves_wflags_and_zeroes_split_off(self):
        with_dirs = Path(self._get_tmp_dir())
        pristine_path = with_dirs / "OBJINFO.DAT"
        json_path = with_dirs / "OBJINFO.json"
        out_path = with_dirs / "out.DAT"
        mapping_path = with_dirs / "zh_mapping.json"

        source_name = "Long Sword"
        pristine = self._make_pristine(source_name.encode("ascii") + b"\x00", wflags=0x1008, split_off=6)
        pristine_path.write_bytes(pristine)

        translated_name = "長剣"  # "長劍"
        json_path.write_text(json.dumps({
            "format": "BAK_ZH_OBJINFO_TRANSLATION",
            "version": 1,
            "source_file": "OBJINFO.DAT",
            "entries": [{
                "id": "OBJINFO.DAT#1", "index": 1, "source": source_name,
                "translation": translated_name, "status": "translated", "notes": "",
            }],
        }), encoding="utf-8")
        mapping_path.write_text(json.dumps({"char_to_id": {"長": 0, "剣": 1}}), encoding="utf-8")

        args = argparse.Namespace(
            objinfo_path=str(pristine_path), json_path=str(json_path),
            out=str(out_path), mapping=str(mapping_path),
        )
        ot.cmd_build(args)

        built = out_path.read_bytes()
        rec = built[ot.RECORD_SIZE: 2 * ot.RECORD_SIZE]
        wflags, split_off = struct.unpack_from("<HH", rec, 32)
        self.assertEqual(wflags, 0x1008, "wFlags must be untouched by translation")
        self.assertEqual(split_off, 0, "wName_split_off must be reset for the re-encoded name")
        self.assertNotEqual(rec[:2], source_name[:2].encode("ascii"), "pName must be re-encoded")

    def _get_tmp_dir(self) -> str:
        import tempfile
        d = tempfile.mkdtemp()
        self.addCleanup(lambda: __import__("shutil").rmtree(d, ignore_errors=True))
        return d


if __name__ == "__main__":
    unittest.main()
