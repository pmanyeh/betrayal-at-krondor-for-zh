"""
Unit tests for the Phase 6 DDX translation pipeline (tools/text/ddx_translate.py).
Covers token extraction (the structural markers a translation must
reproduce exactly) and the scaffold/build round-trip, using small
synthetic DDX payloads so no real game data is required.
"""

import contextlib
import io
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "text"))
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "tools" / "font"))

from ddx_pack import pack_ddx_data  # noqa: E402
from ddx_translate import extract_tokens, cmd_build, cmd_scaffold  # noqa: E402
from build_font import glyph_id_to_bytes  # noqa: E402


def make_ddx(records: list[dict]) -> bytes:
    """Builds a minimal DDX payload: every record is directory-keyed by
    its index, with no choices/opcodes, matching pack_ddx_data's schema."""
    data = {
        "dir_entries": [(1000 + i, r.get("orig_offset", 0)) for i, r in enumerate(records)],
        "records": [
            {
                "orig_offset": i,
                "style": 0,
                "speaker_id": 0,
                "flags": 0,
                "choices": [],
                "opcodes": [],
                "text": r["text"],
            }
            for i, r in enumerate(records)
        ],
    }
    return pack_ddx_data(data)


class TestExtractTokens(unittest.TestCase):
    def test_speaker_tokens(self):
        self.assertEqual(extract_tokens("hi @0 and @1!"), ["@0", "@1"])

    def test_bare_at_sign(self):
        self.assertEqual(extract_tokens("look @ me"), ["@"])

    def test_control_and_terminator_bytes(self):
        text = "\tHello\nWorld\x00"
        self.assertEqual(extract_tokens(text), ["\\x09", "\\x0a", "\\x00"])

    def test_high_control_byte(self):
        text = "before\xe0after"
        self.assertEqual(extract_tokens(text), ["\\xe0"])

    def test_no_tokens_in_plain_text(self):
        self.assertEqual(extract_tokens("just plain text."), [])

    def test_chinese_bytes_are_not_tokens(self):
        # 0x80-0xDF (our Chinese lead-byte range) must not be picked up
        # as a structural token, or every translated line would spuriously
        # fail token-identity validation against its untranslated source.
        text = "\x80\x22\x80\x23\x00"
        self.assertEqual(extract_tokens(text), ["\\x00"])


class TestScaffoldAndBuildRoundTrip(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = Path(__file__).resolve().parent / "_tmp_ddx_translate_test"
        self.tmp_dir.mkdir(exist_ok=True)
        self.ddx_path = self.tmp_dir / "DIAL_Z99.DDX"
        self.json_path = self.tmp_dir / "DIAL_Z99.json"
        self.out_path = self.tmp_dir / "DIAL_Z99_built.DDX"

        self.ddx_path.write_bytes(make_ddx([
            {"text": "\tFirst line.\x00"},
            {"text": "Second line.\x00"},
            {"text": ""},  # empty body, must be skipped by scaffold
        ]))

    def tearDown(self):
        for p in self.tmp_dir.iterdir():
            p.unlink()
        self.tmp_dir.rmdir()

    def _run_scaffold(self):
        class Args:
            ddx_path = str(self.ddx_path)
            out = str(self.json_path)
        cmd_scaffold(Args())

    def _run_build(self, mapping_path):
        class Args:
            ddx_path = str(self.ddx_path)
            json_path = str(self.json_path)
            out = str(self.out_path)
            mapping = str(mapping_path)
        cmd_build(Args())

    def test_scaffold_skips_empty_bodies_and_stores_source_text(self):
        self._run_scaffold()
        data = json.loads(self.json_path.read_text(encoding="utf-8"))
        self.assertEqual(len(data["entries"]), 2)
        self.assertEqual(data["entries"][0]["source"], "\tFirst line.\x00")
        self.assertEqual(data["entries"][1]["source"], "Second line.\x00")
        self.assertEqual(data["entries"][0]["tokens"], ["\\x09", "\\x00"])
        self.assertEqual(data["entries"][1]["tokens"], ["\\x00"])

    def test_rescaffold_warns_on_source_drift(self):
        self._run_scaffold()
        data = json.loads(self.json_path.read_text(encoding="utf-8"))
        data["entries"][0]["source"] = "\tContaminated line.\x00"
        self.json_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            self._run_scaffold()
        self.assertIn("DIAL_Z99.DDX#0", stderr.getvalue())
        self.assertIn("DIFFERENT source text", stderr.getvalue())

        reloaded = json.loads(self.json_path.read_text(encoding="utf-8"))
        # scaffold always re-trusts the local DDX for source text going forward.
        self.assertEqual(reloaded["entries"][0]["source"], "\tFirst line.\x00")

    def test_scaffold_preserves_existing_translations_on_rerun(self):
        self._run_scaffold()
        data = json.loads(self.json_path.read_text(encoding="utf-8"))
        data["entries"][0]["translation"] = "\t\x80\x22\x00"
        data["entries"][0]["status"] = "translated"
        self.json_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

        self._run_scaffold()
        reloaded = json.loads(self.json_path.read_text(encoding="utf-8"))
        self.assertEqual(reloaded["entries"][0]["status"], "translated")
        self.assertEqual(reloaded["entries"][0]["translation"], "\t\x80\x22\x00")

    def test_build_applies_translation_and_falls_back_on_mismatch(self):
        char_to_id = {"我": 0}
        mapping_path = self.tmp_dir / "mapping.json"
        mapping_path.write_text(json.dumps({"char_to_id": char_to_id}), encoding="utf-8")

        self._run_scaffold()
        data = json.loads(self.json_path.read_text(encoding="utf-8"))
        # Entry 0 ("\tFirst line.\x00", tokens \x09 \x00): valid translation, same tokens.
        # The JSON stores literal Chinese characters; cmd_build does the BAK-ZH encoding.
        data["entries"][0]["translation"] = "\t我\x00"
        data["entries"][0]["status"] = "translated"
        # Entry 1 ("Second line.\x00", tokens \x00): translation drops the \x00 terminator token -> mismatch.
        data["entries"][1]["translation"] = "我"
        data["entries"][1]["status"] = "translated"
        self.json_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

        self._run_build(mapping_path)

        from ddx_extract import extract_ddx_data
        built = extract_ddx_data(self.out_path.read_bytes())
        gid_bytes = glyph_id_to_bytes(0).decode("latin1")
        self.assertEqual(built["records"][0]["text"], "\t" + gid_bytes + "\x00")
        # Token mismatch on entry 1 must fall back to the original source text untouched.
        self.assertEqual(built["records"][1]["text"], "Second line.\x00")

    def test_build_falls_back_when_local_ddx_source_drifted(self):
        # Guards the exact failure mode found in this project: a "translated"
        # entry whose recorded source no longer matches the local DDX (e.g. it
        # was scaffolded from a contaminated copy) must never be silently
        # trusted at build time.
        char_to_id = {"我": 0}
        mapping_path = self.tmp_dir / "mapping.json"
        mapping_path.write_text(json.dumps({"char_to_id": char_to_id}), encoding="utf-8")

        self._run_scaffold()
        data = json.loads(self.json_path.read_text(encoding="utf-8"))
        data["entries"][0]["source"] = "\tContaminated line.\x00"
        data["entries"][0]["translation"] = "\t我\x00"
        data["entries"][0]["status"] = "translated"
        self.json_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr):
            self._run_build(mapping_path)
        self.assertIn("source text on file doesn't match", stderr.getvalue())

        from ddx_extract import extract_ddx_data
        built = extract_ddx_data(self.out_path.read_bytes())
        self.assertEqual(built["records"][0]["text"], "\tFirst line.\x00")

    def test_status_reads_only_the_json(self):
        self._run_scaffold()
        data = json.loads(self.json_path.read_text(encoding="utf-8"))
        data["entries"][0]["translation"] = "我"
        data["entries"][0]["status"] = "translated"
        self.json_path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

        from ddx_translate import cmd_status

        class Args:
            json_path = str(self.json_path)
            show_untranslated = True

        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            cmd_status(Args())
        out = stdout.getvalue()
        self.assertIn("translated: 1", out)
        self.assertIn("untranslated: 1", out)
        self.assertIn("Second line.", out)


if __name__ == "__main__":
    unittest.main()
