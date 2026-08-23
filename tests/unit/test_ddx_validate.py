"""Tests for structural DDX validation and all-or-nothing rebuild behavior."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from tools.text.ddx_pack import pack_ddx_data
from tools.text.ddx_rebuild_all import rebuild_all
from tools.text.ddx_validate import DdxValidationError, validate_ddx_data


def _one_record_ddx() -> bytes:
    return pack_ddx_data({
        "dir_entries": [(1000, 0)],
        "records": [{
            "orig_offset": 0,
            "style": 0,
            "speaker_id": 0,
            "flags": 0,
            "choices": [],
            "opcodes": [],
            "text": "English\x00",
        }],
    })


class TestDdxValidation(unittest.TestCase):
    def test_rejects_dangling_directory_target(self):
        payload = bytearray(_one_record_ddx())
        payload[6:10] = (0x12345678).to_bytes(4, "little")
        with self.assertRaisesRegex(DdxValidationError, "directory entry"):
            validate_ddx_data(bytes(payload))

    def test_rejects_dangling_choice_target(self):
        payload = pack_ddx_data({
            "dir_entries": [(1000, 0)],
            "records": [{
                "orig_offset": 0,
                "style": 0,
                "speaker_id": 0,
                "flags": 0,
                "choices": [{"wCond": 0, "nA1": 0, "nA2": 0, "nA3": 0x1234, "nA4": 0}],
                "opcodes": [],
                "text": "English\x00",
            }],
        })
        with self.assertRaisesRegex(DdxValidationError, "choice 0"):
            validate_ddx_data(payload)

    def test_accepts_global_keyed_choice_target(self):
        payload = pack_ddx_data({
            "dir_entries": [(1000, 0)],
            "records": [{
                "orig_offset": 0,
                "style": 0,
                "speaker_id": 0,
                "flags": 0,
                "choices": [{"wCond": 0, "nA1": 0, "nA2": 0, "nA3": 0x00C4, "nA4": 0x8000}],
                "opcodes": [],
                "text": "English\x00",
            }],
        })
        summary = validate_ddx_data(payload)
        self.assertEqual(summary["external_choice_targets"], 1)

    def test_rebuild_refuses_partial_input_without_touching_output(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            source = root / "pristine"
            translated = root / "translated"
            output = root / "out"
            source.mkdir()
            translated.mkdir()
            output.mkdir()
            (source / "DIAL_Z00.DDX").write_bytes(_one_record_ddx())
            (output / "DIAL_Z00.DDX").write_bytes(b"old-output")
            mapping = root / "mapping.json"
            mapping.write_text(json.dumps({"char_to_id": {}}), encoding="utf-8")
            for name in ("DIAL_Z00", "DIAL_Z01"):
                (translated / f"{name}.json").write_text(json.dumps({
                    "format": "BAK_ZH_TRANSLATION", "version": 1,
                    "source_ddx": f"{name}.DDX", "entries": [],
                }), encoding="utf-8")

            with self.assertRaisesRegex(ValueError, "refusing partial rebuild"):
                rebuild_all(source, translated, output, mapping)
            self.assertEqual((output / "DIAL_Z00.DDX").read_bytes(), b"old-output")


if __name__ == "__main__":
    unittest.main()
