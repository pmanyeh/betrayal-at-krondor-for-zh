"""Shared, importable implementation for one translated DDX build."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

# These tools are runnable both as ``python tools/text/<tool>.py`` and as
# importable test modules.  Make the sibling font tool available in either
# invocation mode.
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "font"))

from build_font import encode_string
try:  # Direct script execution
    from ddx_extract import extract_ddx_data
    from ddx_pack import pack_ddx_data
    from ddx_validate import validate_ddx_data
except ModuleNotFoundError:  # ``from tools.text...`` in unit tests
    from tools.text.ddx_extract import extract_ddx_data
    from tools.text.ddx_pack import pack_ddx_data
    from tools.text.ddx_validate import validate_ddx_data

_TOKEN_RE = re.compile(r"@\d|@|[\x00-\x1f\xe0-\xff]")


def extract_tokens(text: str) -> list[str]:
    tokens = []
    for match in _TOKEN_RE.finditer(text):
        value = match.group(0)
        if len(value) == 1 and (ord(value) < 0x20 or ord(value) >= 0xE0):
            tokens.append(f"\\x{ord(value):02x}")
        else:
            tokens.append(value)
    return tokens


def _entry_id(ddx_name: str, rec_index: int) -> str:
    return f"{ddx_name}#{rec_index}"


def _preview(source: str, width: int = 70) -> str:
    return "".join(c if 0x20 <= ord(c) < 0x7F else f"\\x{ord(c):02x}" for c in source[:width])


def build_ddx_file(ddx_path: Path, json_path: Path, out_path: Path, mapping_path: Path) -> dict[str, int]:
    """Build, validate, then write one localized DDX file."""
    ddx_name = ddx_path.name
    payload = ddx_path.read_bytes()
    validate_ddx_data(payload, label=str(ddx_path))
    extracted = extract_ddx_data(payload)
    data: dict[str, Any] = json.loads(json_path.read_text(encoding="utf-8"))
    if data.get("source_ddx") != ddx_name:
        print(
            f"warning: translation file was scaffolded from {data.get('source_ddx')!r}, "
            f"building against {ddx_name!r}",
            file=sys.stderr,
        )
    translations = {entry["id"]: entry for entry in data.get("entries", [])}
    char_to_id = json.loads(mapping_path.read_text(encoding="utf-8"))["char_to_id"]

    applied = skipped_untranslated = skipped_token_mismatch = skipped_source_drift = 0
    for record in extracted["records"]:
        entry_id = _entry_id(ddx_name, record["rec_index"])
        entry = translations.get(entry_id)
        if entry is None or entry["status"] != "translated" or not entry["translation"]:
            if entry is not None and entry["status"] != "untranslated" and not entry["translation"]:
                skipped_untranslated += 1
            continue
        if entry.get("source") != record["text"]:
            print(
                f"warning: {entry_id} source text on file doesn't match the local DDX you're building "
                f"against, falling back to the local DDX's text\n"
                f"  on file: {_preview(entry.get('source', ''))}\n"
                f"  local:   {_preview(record['text'])}",
                file=sys.stderr,
            )
            skipped_source_drift += 1
            continue
        source_tokens = extract_tokens(record["text"])
        translation_tokens = extract_tokens(entry["translation"])
        if source_tokens != translation_tokens:
            print(
                f"warning: {entry_id} token mismatch, falling back to source text\n"
                f"  source tokens:      {source_tokens}\n"
                f"  translation tokens: {translation_tokens}",
                file=sys.stderr,
            )
            skipped_token_mismatch += 1
            continue
        record["text"] = encode_string(entry["translation"], char_to_id).decode("latin1")
        applied += 1

    packed = pack_ddx_data(extracted)
    validate_ddx_data(packed, label=str(out_path))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(packed)
    return {
        "applied": applied,
        "skipped_untranslated": skipped_untranslated,
        "skipped_token_mismatch": skipped_token_mismatch,
        "skipped_source_drift": skipped_source_drift,
    }
