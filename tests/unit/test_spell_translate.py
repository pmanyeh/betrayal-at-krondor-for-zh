import argparse
import json
import struct
import tempfile
import unittest
from pathlib import Path

from tools.text import spell_translate as st


def make_spells_dat(names):
    """count | count*22-byte SpellDef (u16 name-offset + 10 i16) | u16 size field | name pool"""
    pool = bytearray()
    offsets = []
    for n in names:
        offsets.append(len(pool))
        pool += n.encode("latin1") + b"\0"
    recs = bytearray()
    for off in offsets:
        recs += struct.pack("<H", off) + b"\0" * 20
    body = struct.pack("<H", len(names)) + bytes(recs)
    size_field_at = len(body) + 0  # follows the records
    out = body + struct.pack("<H", 0) + bytes(pool)
    out = bytearray(out)
    struct.pack_into("<H", out, len(body), len(out) & 0xFFFF)
    return bytes(out)


def make_spelldoc_dat(rows):
    """rowCount | rowCount*u32 offset | u16 size field | string pool (deduped)"""
    pool = bytearray()
    interned = {}
    offsets = []
    for r in rows:
        key = r.encode("latin1")
        if key not in interned:
            interned[key] = len(pool)
            pool += key + b"\0"
        offsets.append(interned[key])
    body = struct.pack("<H", len(rows)) + struct.pack("<" + "I" * len(rows), *offsets)
    out = bytearray(body + struct.pack("<H", 0) + bytes(pool))
    struct.pack_into("<H", out, len(body), len(out) & 0xFFFF)
    return bytes(out)


def make_invspell_dat(panels):
    """6 panels: u16 icon | u16 count | count*(char[24] name + u16 spellIdx)"""
    out = bytearray()
    for icon, recs in panels:
        out += struct.pack("<HH", icon, len(recs))
        for name, idx in recs:
            enc = name.encode("latin1")
            out += enc + b"\0" * (24 - len(enc)) + struct.pack("<H", idx)
    return bytes(out)


SPELL_NAMES = ["Flamecast", "Skyfire", "Candle Glow"]
DOC_ROWS = [
    "Flamecast", "Cost: 1-20 Health/Stamina", "Damage: 3 x Cost", "", "Line of sight: Yes",
    "Area fire damage", "",
    "Skyfire", "Cost: 12 Health/Stamina", "Damage: 40", "", "Line of sight: No",
    "Opponent must be carrying metal", "",
    "Candle Glow", "Cost: 1-15 Health", "", "Duration: 48 minutes X Cost", "",
    "Creates light below ground", "",
]
PANELS = [
    (37, [("Flamecast", 0), ("Skyfire", 1)]),
    (36, [("Candle Glow", 2)]),
    (38, []), (39, []), (55, []), (56, []),
]


class TestSpellCodec(unittest.TestCase):
    def test_decoders(self):
        _c, names = st.decode_spells_dat(make_spells_dat(SPELL_NAMES))
        self.assertEqual(names, SPELL_NAMES)
        rows, strings = st.decode_spelldoc_dat(make_spelldoc_dat(DOC_ROWS))
        self.assertEqual(rows, len(DOC_ROWS))
        self.assertEqual(strings, DOC_ROWS)
        panels = st.decode_invspell_dat(make_invspell_dat(PANELS))
        self.assertEqual([r["name"] for r in panels[0]], ["Flamecast", "Skyfire"])
        self.assertEqual(panels[0][1]["spell_idx"], 1)


class TestSpellBuild(unittest.TestCase):
    def _run(self, entries, *, mapping=None):
        tmp = Path(self.tmp.name)
        spells = tmp / "SPELLS.DAT"
        spelldoc = tmp / "SPELLDOC.DAT"
        invspell = tmp / "INVSPELL.DAT"
        catalog = tmp / "SPELLS.json"
        mapfile = tmp / "mapping.json"
        outdir = tmp / "out"
        spells.write_bytes(make_spells_dat(SPELL_NAMES))
        spelldoc.write_bytes(make_spelldoc_dat(DOC_ROWS))
        invspell.write_bytes(make_invspell_dat(PANELS))
        catalog.write_text(json.dumps({"entries": entries}, ensure_ascii=False), encoding="utf-8")
        mapfile.write_text(json.dumps({"char_to_id": mapping or {}}), encoding="utf-8")
        st.cmd_build(argparse.Namespace(
            spells=str(spells), spelldoc=str(spelldoc), invspell=str(invspell),
            json_path=str(catalog), out_dir=str(outdir), mapping=str(mapfile),
        ))
        return (
            (outdir / "SPELLS.DAT").read_bytes(),
            (outdir / "SPELLDOC.DAT").read_bytes(),
            (outdir / "INVSPELL.DAT").read_bytes(),
        )

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)

    def test_untranslated_build_is_byte_identical(self):
        s, d, i = self._run([])
        self.assertEqual(s, make_spells_dat(SPELL_NAMES))
        self.assertEqual(d, make_spelldoc_dat(DOC_ROWS))
        self.assertEqual(i, make_invspell_dat(PANELS))

    def test_translation_appends_and_repoints(self):
        mapping = {"擲": 0, "焰": 1, "術": 2, "天": 3, "火": 4}
        entries = [
            {"id": "SPELLS.DAT#0", "source": "Flamecast", "translation": "擲焰術",
             "status": "translated"},
            {"id": "SPELLDOC.DAT#0.0", "source": "Flamecast", "translation": "擲焰術",
             "status": "translated"},
            {"id": "INVSPELL.DAT#0.0", "source": "Flamecast", "translation": "擲焰術",
             "status": "translated"},
        ]
        s, d, i = self._run(entries, mapping=mapping)
        zh = st.encode_string("擲焰術", mapping).decode("latin1")
        _c, names = st.decode_spells_dat(s)
        self.assertEqual(names[0], zh)                   # repointed to appended string
        self.assertEqual(names[1], "Skyfire")            # untouched
        self.assertEqual(names[2], "Candle Glow")        # untouched
        # append-only: the original English bytes stay in the pool, only the
        # record's offset moves to the freshly appended copy at end-of-file.
        recs_end = 2 + 3 * st.SPELLDEF_SIZE
        orig_pool_len = len(make_spells_dat(SPELL_NAMES)) - recs_end - 2
        self.assertGreaterEqual(int.from_bytes(s[2:4], "little"), orig_pool_len)
        # size field still tracks the (grown) file length
        self.assertEqual(int.from_bytes(s[recs_end:recs_end + 2], "little"), len(s))
        self.assertGreater(len(s), len(make_spells_dat(SPELL_NAMES)))
        _r, strings = st.decode_spelldoc_dat(d)
        self.assertEqual(strings[0], zh)
        self.assertEqual(strings[7], "Skyfire")          # untouched row
        panels = st.decode_invspell_dat(i)
        self.assertEqual(panels[0][0]["name"], zh)
        self.assertEqual(len(i), len(make_invspell_dat(PANELS)))  # patched in place

    def test_source_drift_falls_back_to_english(self):
        entries = [{"id": "SPELLS.DAT#0", "source": "Fireball", "translation": "火球",
                    "status": "translated"}]
        s, _d, _i = self._run(entries, mapping={"火": 0, "球": 1})
        _c, names = st.decode_spells_dat(s)
        self.assertEqual(names[0], "Flamecast")

    def test_overlong_spelldoc_line_falls_back(self):
        long_zh = "字" * 40  # 40 * 2 bytes = 80 > SPELLDOC_LINE_BUDGET
        entries = [{"id": "SPELLDOC.DAT#0.5", "source": "Area fire damage",
                    "translation": long_zh, "status": "translated"}]
        _s, d, _i = self._run(entries, mapping={"字": 0})
        _r, strings = st.decode_spelldoc_dat(d)
        self.assertEqual(strings[5], "Area fire damage")

    def test_overlong_invspell_name_falls_back(self):
        long_zh = "字" * 13  # 26 bytes > 23-byte field budget
        entries = [{"id": "INVSPELL.DAT#0.0", "source": "Flamecast",
                    "translation": long_zh, "status": "translated"}]
        _s, _d, i = self._run(entries, mapping={"字": 0})
        panels = st.decode_invspell_dat(i)
        self.assertEqual(panels[0][0]["name"], "Flamecast")


if __name__ == "__main__":
    unittest.main()
