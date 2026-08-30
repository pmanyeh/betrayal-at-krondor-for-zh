import argparse
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.text import mnames_translate as mt


def make_mnames_dat(names):
    """u16 count | count*u16 offset | u16 size-field | deduped NUL string pool"""
    pool = bytearray()
    interned = {}
    offsets = []
    for n in names:
        key = n.encode("latin1")
        if key not in interned:
            interned[key] = len(pool)
            pool += key + b"\0"
        offsets.append(interned[key])
    body = struct.pack("<H", len(names)) + struct.pack("<" + "H" * len(names), *offsets)
    out = bytearray(body + struct.pack("<H", 0) + bytes(pool))
    struct.pack_into("<H", out, len(body), len(out) & 0xFFFF)
    return bytes(out)


NAMES = ["INVALID MONSTER", "Gorath", "moredhel warrior", "INVALID MONSTER", "Black Slayer"]


class TestMnamesCodec(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(mt.decode_mnames_dat(make_mnames_dat(NAMES)), NAMES)

    def test_dedup_placeholders_share_one_string(self):
        raw = make_mnames_dat(NAMES)
        # only one "INVALID MONSTER" copy in the pool
        self.assertEqual(raw.count(b"INVALID MONSTER"), 1)


class TestMnamesBuild(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def _run(self, entries, mapping):
        root = Path(self.tmp.name)
        src = root / "MNAMES.DAT"
        cat = root / "MNAMES.json"
        mp = root / "map.json"
        out = root / "out.DAT"
        src.write_bytes(make_mnames_dat(NAMES))
        cat.write_text(json.dumps({"entries": entries}, ensure_ascii=False), encoding="utf-8")
        mp.write_text(json.dumps({"char_to_id": mapping}), encoding="utf-8")
        mt.cmd_build(argparse.Namespace(
            mnames_path=str(src), json_path=str(cat), out=str(out), mapping=str(mp)))
        return out.read_bytes()

    def test_untranslated_build_is_byte_identical(self):
        self.assertEqual(self._run([], {}), make_mnames_dat(NAMES))

    def test_translation_appends_and_repoints(self):
        mapping = {"莫": 0, "瑞": 1, "德": 2, "戰": 3, "士": 4}
        entries = [{"id": "MNAMES.DAT#2", "source": "moredhel warrior",
                    "translation": "莫瑞德戰士", "status": "translated"}]
        raw = self._run(entries, mapping)
        got = mt.decode_mnames_dat(raw)
        self.assertEqual(got[1], "Gorath")                 # untouched
        self.assertEqual(got[0], "INVALID MONSTER")        # untouched
        self.assertEqual(got[2], mt.encode_string("莫瑞德戰士", mapping).decode("latin1"))
        self.assertGreater(len(raw), len(make_mnames_dat(NAMES)))  # pool grew
        # size field still equals file length
        n = len(NAMES)
        self.assertEqual(int.from_bytes(raw[2 + n * 2:2 + n * 2 + 2], "little"), len(raw))

    def test_source_drift_falls_back(self):
        entries = [{"id": "MNAMES.DAT#1", "source": "Groath",
                    "translation": "戈", "status": "translated"}]
        got = mt.decode_mnames_dat(self._run(entries, {"戈": 0}))
        self.assertEqual(got[1], "Gorath")

    def test_overlong_name_falls_back(self):
        entries = [{"id": "MNAMES.DAT#1", "source": "Gorath",
                    "translation": "字" * 16, "status": "translated"}]  # 32 bytes > 31
        got = mt.decode_mnames_dat(self._run(entries, {"字": 0}))
        self.assertEqual(got[1], "Gorath")


if __name__ == "__main__":
    unittest.main()
