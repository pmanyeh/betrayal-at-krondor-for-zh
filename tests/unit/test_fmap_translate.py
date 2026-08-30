import argparse
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.text import fmap_translate as ft


def make_fmap_twn(towns):
    """towns: list of (name, x, y). Header is mapW/mapH/hotW/hotH/count."""
    out = bytearray(struct.pack("<HHHHH", 3, 3, 9, 9, len(towns)))
    for name, x, y in towns:
        body = name.encode("latin1") + b"\0"
        out += struct.pack("<H", len(body)) + body + struct.pack("<HH", x, y)
    return bytes(out)


TOWNS = [("LaMut", 106, 86), ("Krondor", 167, 147), ("Eldpoint", 180, 70)]


class TestFmapCodec(unittest.TestCase):
    def test_decode(self):
        self.assertEqual(ft.decode_fmap_twn(make_fmap_twn(TOWNS)),
                         ["LaMut", "Krondor", "Eldpoint"])

    def test_trailing_bytes_rejected(self):
        with self.assertRaises(ValueError):
            ft.decode_fmap_twn(make_fmap_twn(TOWNS) + b"\x00")


class TestFmapBuild(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def _run(self, entries, mapping):
        root = Path(self.tmp.name)
        src = root / "fmap_twn.dat"
        cat = root / "FMAP_TWN.json"
        mp = root / "map.json"
        out = root / "out.dat"
        src.write_bytes(make_fmap_twn(TOWNS))
        cat.write_text(json.dumps({"entries": entries}, ensure_ascii=False), encoding="utf-8")
        mp.write_text(json.dumps({"char_to_id": mapping}), encoding="utf-8")
        ft.cmd_build(argparse.Namespace(
            fmap_path=str(src), json_path=str(cat), out=str(out), mapping=str(mp)))
        return out.read_bytes()

    def test_untranslated_build_is_byte_identical(self):
        self.assertEqual(self._run([], {}), make_fmap_twn(TOWNS))

    def test_translation_rewrites_record_and_keeps_coords(self):
        mapping = {"克": 0, "朗": 1, "多": 2}
        entries = [{"id": "FMAP_TWN.DAT#1", "source": "Krondor",
                    "translation": "克朗多", "status": "translated"}]
        raw = self._run(entries, mapping)
        names = ft.decode_fmap_twn(raw)
        self.assertEqual(names[0], "LaMut")   # untouched
        self.assertEqual(names[2], "Eldpoint")
        self.assertEqual(names[1], ft.encode_string("克朗多", mapping).decode("latin1"))
        # coords for Krondor preserved
        _hdr, recs = ft._iter_records(raw)
        self.assertEqual((recs[1]["x"], recs[1]["y"]), (167, 147))
        # header town count unchanged
        self.assertEqual(struct.unpack_from("<H", raw, 8)[0], 3)

    def test_source_drift_falls_back(self):
        entries = [{"id": "FMAP_TWN.DAT#0", "source": "Lamut",
                    "translation": "拉", "status": "translated"}]
        self.assertEqual(ft.decode_fmap_twn(self._run(entries, {"拉": 0}))[0], "LaMut")

    def test_overlong_falls_back(self):
        entries = [{"id": "FMAP_TWN.DAT#0", "source": "LaMut",
                    "translation": "字" * 40, "status": "translated"}]  # 80+1 bytes > 62
        self.assertEqual(ft.decode_fmap_twn(self._run(entries, {"字": 0}))[0], "LaMut")


if __name__ == "__main__":
    unittest.main()
