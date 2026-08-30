import argparse
import json
import tempfile
import unittest
from pathlib import Path

from tools.text import keyword_translate as kt


class TestKeywordTranslate(unittest.TestCase):
    def test_codec_preserves_slots_and_deduplicates_strings(self):
        blob = kt.encode_keyword_dat([b"Inns", b"", b"Inns", b"GoodBye"])
        self.assertEqual(kt.decode_keyword_dat(blob), ["Inns", "", "Inns", "GoodBye"])
        self.assertEqual(int.from_bytes(blob[:2], "little"), len(blob))

    def test_build_translates_by_stable_one_based_index(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "KEYWORD.DAT"
            catalog = root / "KEYWORD.json"
            mapping = root / "mapping.json"
            output = root / "out.DAT"
            source.write_bytes(kt.encode_keyword_dat([b"Inns", b"", b"Cancel"]))
            catalog.write_text(
                json.dumps(
                    {
                        "entries": [
                            {
                                "id": "KEYWORD.DAT#1",
                                "source": "Inns",
                                "translation": "旅店",
                                "status": "translated",
                            },
                            {
                                "id": "KEYWORD.DAT#3",
                                "source": "Cancel",
                                "translation": "取消",
                                "status": "translated",
                            },
                        ]
                    },
                    ensure_ascii=False,
                ),
                encoding="utf-8",
            )
            mapping.write_text(
                json.dumps({"char_to_id": {"旅": 0, "店": 1, "取": 2, "消": 3}}),
                encoding="utf-8",
            )
            kt.cmd_build(
                argparse.Namespace(
                    keyword_path=str(source),
                    json_path=str(catalog),
                    out=str(output),
                    mapping=str(mapping),
                )
            )
            raw = output.read_bytes()
            size, count = int.from_bytes(raw[:2], "little"), int.from_bytes(raw[2:4], "little")
            self.assertEqual(size, len(raw))
            self.assertEqual(count, 3)
            self.assertEqual(kt.decode_keyword_dat(raw)[1], "")
            self.assertNotIn(b"Inns", raw)
            self.assertNotIn(b"Cancel", raw)


if __name__ == "__main__":
    unittest.main()
