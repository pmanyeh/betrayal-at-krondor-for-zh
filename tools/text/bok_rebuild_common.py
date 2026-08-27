"""Shared, importable implementation for one translated BOK build."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "font"))

from build_font import encode_string

try:  # Direct script execution
    from bok_extract import extract_bok_data
    from bok_pack import pack_bok_data, validate_bok_data
    from ddx_rebuild_common import extract_tokens
except ModuleNotFoundError:  # ``from tools.text...`` in unit tests
    from tools.text.bok_extract import extract_bok_data
    from tools.text.bok_pack import pack_bok_data, validate_bok_data
    from tools.text.ddx_rebuild_common import extract_tokens


def entry_id(bok_name: str, page_index: int, run_index: int) -> str:
    return f"{bok_name}#{page_index}#{run_index}"


def _preview(source: str, width: int = 70) -> str:
    return "".join(c if 0x20 <= ord(c) < 0x7F else f"\\x{ord(c):02x}" for c in source[:width])


def iter_runs(extracted: dict[str, Any]):
    """Yield (page_index, run_index, stream_item) for every text run."""
    for page in extracted["pages"]:
        for item in page["stream"]:
            if item["kind"] == "text":
                yield page["index"], item["run_index"], item


def build_bok_file(bok_path: Path, json_path: Path, out_path: Path, mapping_path: Path) -> dict[str, int]:
    """Build, validate, then write one localized BOK file."""
    bok_name = bok_path.name
    extracted = extract_bok_data(bok_path.read_bytes())

    data: dict[str, Any] = json.loads(json_path.read_text(encoding="utf-8"))
    if data.get("source_bok") != bok_name:
        print(
            f"warning: translation file was scaffolded from {data.get('source_bok')!r}, "
            f"building against {bok_name!r}",
            file=sys.stderr,
        )
    translations = {e["id"]: e for e in data.get("entries", [])}
    char_to_id = json.loads(mapping_path.read_text(encoding="utf-8"))["char_to_id"]

    applied = skipped_untranslated = skipped_token_mismatch = skipped_source_drift = 0
    for page_index, run_index, item in iter_runs(extracted):
        eid = entry_id(bok_name, page_index, run_index)
        entry = translations.get(eid)
        if entry is None or entry["status"] != "translated" or not entry["translation"]:
            if entry is not None and entry["status"] != "untranslated" and not entry["translation"]:
                skipped_untranslated += 1
            continue
        if entry.get("source") != item["text"]:
            print(
                f"warning: {eid} source text on file doesn't match the local BOK you're building "
                f"against, falling back to the local BOK's text\n"
                f"  on file: {_preview(entry.get('source', ''))}\n"
                f"  local:   {_preview(item['text'])}",
                file=sys.stderr,
            )
            skipped_source_drift += 1
            continue
        if extract_tokens(item["text"]) != extract_tokens(entry["translation"]):
            print(
                f"warning: {eid} token mismatch, falling back to source text\n"
                f"  source tokens:      {extract_tokens(item['text'])}\n"
                f"  translation tokens: {extract_tokens(entry['translation'])}",
                file=sys.stderr,
            )
            skipped_token_mismatch += 1
            continue
        item["text"] = encode_string(entry["translation"], char_to_id).decode("latin1")
        applied += 1

    packed = pack_bok_data(extracted)
    validate_bok_data(packed, label=str(out_path))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(packed)
    return {
        "applied": applied,
        "skipped_untranslated": skipped_untranslated,
        "skipped_token_mismatch": skipped_token_mismatch,
        "skipped_source_drift": skipped_source_drift,
    }
