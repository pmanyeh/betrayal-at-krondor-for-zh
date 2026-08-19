#!/usr/bin/env python3
"""
Betrayal at Krondor — DDX Translation Pipeline (Phase 6)

Canonical translation files under localization/translated/*.json store
the id/source/translation/status/notes/tokens for each DDX text record,
so a translation can be reviewed side by side with its English source
directly in the tracked file. Because the source text is committed,
`scaffold` and `build` both re-read the user's local DDX and compare it
against whatever source text is already on file, warning loudly on any
mismatch — this is exactly how a stale or contaminated local copy of
the "pristine" game data was caught once already in this project.

Pipeline: original DDX (local, gitignored)
          -> scaffold  -> localization/translated/<CHAPTER>.json (tracked, includes source text)
          -> (human/agent fills in "translation" + "status")
          -> build     -> localized DDX (build output, gitignored)
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "font"))

from ddx_extract import extract_ddx_data  # noqa: E402
from ddx_pack import pack_ddx_data  # noqa: E402
from build_font import encode_string  # noqa: E402

_TOKEN_RE = re.compile(r"@\d|@|[\x00-\x1f\xe0-\xff]")

_DEFAULT_MAPPING = Path(__file__).resolve().parents[2] / "localization" / "generated" / "zh_mapping.json"


def extract_tokens(text: str) -> list[str]:
    """Structural markers a translation must reproduce exactly: speaker
    tokens (@0, @1, ...), control/style bytes (0xE0-0xFF), and raw
    control characters like \\t / \\n. Encoded as \\xNN for the
    non-printable single bytes so the token list is JSON-safe."""
    tokens = []
    for m in _TOKEN_RE.finditer(text):
        s = m.group(0)
        if len(s) == 1 and ord(s) < 0x20 or (len(s) == 1 and ord(s) >= 0xE0):
            tokens.append(f"\\x{ord(s):02x}")
        else:
            tokens.append(s)
    return tokens


def _entry_id(ddx_name: str, rec_index: int) -> str:
    return f"{ddx_name}#{rec_index}"


def cmd_scaffold(args: argparse.Namespace) -> None:
    ddx_path = Path(args.ddx_path)
    ddx_name = ddx_path.name
    payload = ddx_path.read_bytes()
    extracted = extract_ddx_data(payload)

    out_path = Path(args.out) if args.out else Path("localization/translated") / (ddx_path.stem + ".json")

    existing: dict[str, dict[str, Any]] = {}
    if out_path.exists():
        prior = json.loads(out_path.read_text(encoding="utf-8"))
        for e in prior.get("entries", []):
            existing[e["id"]] = e

    new_entries = []
    seen_ids = set()
    drifted = []
    for rec in extracted["records"]:
        if not rec["text"]:
            continue
        entry_id = _entry_id(ddx_name, rec["rec_index"])
        seen_ids.add(entry_id)
        tokens = extract_tokens(rec["text"])
        prior_entry = existing.get(entry_id)
        if prior_entry is not None and prior_entry.get("source") != rec["text"]:
            drifted.append(entry_id)
        new_entries.append({
            "id": entry_id,
            "node_id": rec["node_id"],
            "source": rec["text"],
            "tokens": tokens,
            "translation": prior_entry["translation"] if prior_entry else "",
            "status": prior_entry["status"] if prior_entry else "untranslated",
            "notes": prior_entry["notes"] if prior_entry else "",
        })

    stale_ids = set(existing) - seen_ids
    if stale_ids:
        print(f"warning: {len(stale_ids)} previously-scaffolded id(s) no longer present in {ddx_name}: "
              f"{sorted(stale_ids)[:10]}{' ...' if len(stale_ids) > 10 else ''}", file=sys.stderr)
    if drifted:
        print(f"warning: {len(drifted)} id(s) have a DIFFERENT source text than what's already on file "
              f"(the local DDX you just read doesn't match {out_path} -- it may be stale, contaminated, or "
              f"you're pointing at the wrong file): {drifted[:10]}{' ...' if len(drifted) > 10 else ''}",
              file=sys.stderr)

    out_data = {
        "format": "BAK_ZH_TRANSLATION",
        "version": 1,
        "source_ddx": ddx_name,
        "entries": new_entries,
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out_data, indent=2, ensure_ascii=False), encoding="utf-8")

    added = sum(1 for e in new_entries if e["id"] not in existing)
    translated = sum(1 for e in new_entries if e["status"] == "translated")
    print(f"Scaffolded {len(new_entries)} entries ({added} new, {translated} already translated) to {out_path}")


def _preview(source: str, width: int = 70) -> str:
    return "".join(
        c if 0x20 <= ord(c) < 0x7F else f"\\x{ord(c):02x}"
        for c in source[:width]
    )


def cmd_status(args: argparse.Namespace) -> None:
    data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    entries = data.get("entries", [])

    by_status: dict[str, int] = {}
    for e in entries:
        by_status[e["status"]] = by_status.get(e["status"], 0) + 1

    print(f"{data.get('source_ddx', '?')}: {len(entries)} entries")
    for status, count in sorted(by_status.items()):
        print(f"  {status}: {count}")

    if args.show_untranslated:
        print("\nUntranslated:")
        for e in entries:
            if e["status"] != "untranslated":
                continue
            print(f"  {e['id']} (node {e['node_id']}): {_preview(e.get('source', ''))}")


def cmd_build(args: argparse.Namespace) -> None:
    ddx_path = Path(args.ddx_path)
    ddx_name = ddx_path.name
    payload = ddx_path.read_bytes()
    extracted = extract_ddx_data(payload)

    data = json.loads(Path(args.json_path).read_text(encoding="utf-8"))
    if data.get("source_ddx") != ddx_name:
        print(f"warning: translation file was scaffolded from {data.get('source_ddx')!r}, "
              f"building against {ddx_name!r}", file=sys.stderr)
    translations = {e["id"]: e for e in data.get("entries", [])}

    mapping = json.loads(Path(args.mapping).read_text(encoding="utf-8"))
    char_to_id = mapping["char_to_id"]

    applied = 0
    skipped_untranslated = 0
    skipped_token_mismatch = 0
    skipped_source_drift = 0

    for rec in extracted["records"]:
        entry_id = _entry_id(ddx_name, rec["rec_index"])
        entry = translations.get(entry_id)
        if entry is None or entry["status"] != "translated" or not entry["translation"]:
            if entry is not None and entry["status"] != "untranslated" and not entry["translation"]:
                skipped_untranslated += 1
            continue

        if entry.get("source") != rec["text"]:
            print(f"warning: {entry_id} source text on file doesn't match the local DDX you're building "
                  f"against, falling back to the local DDX's text\n"
                  f"  on file: {_preview(entry.get('source', ''))}\n"
                  f"  local:   {_preview(rec['text'])}", file=sys.stderr)
            skipped_source_drift += 1
            continue

        source_tokens = extract_tokens(rec["text"])
        translation_tokens = extract_tokens(entry["translation"])
        if source_tokens != translation_tokens:
            print(f"warning: {entry_id} token mismatch, falling back to source text\n"
                  f"  source tokens:      {source_tokens}\n"
                  f"  translation tokens: {translation_tokens}", file=sys.stderr)
            skipped_token_mismatch += 1
            continue

        encoded = encode_string(entry["translation"], char_to_id)
        rec["text"] = encoded.decode("latin1")
        applied += 1

    packed = pack_ddx_data(extracted)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(packed)

    print(f"Built {out_path}: {applied} record(s) translated, "
          f"{skipped_untranslated} marked-but-empty skipped, "
          f"{skipped_token_mismatch} token-mismatch fallback(s), "
          f"{skipped_source_drift} source-drift fallback(s)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Betrayal at Krondor DDX translation pipeline.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_scaffold = sub.add_parser("scaffold", help="Create/update a translation file from a local DDX (stores source text; warns on source drift).")
    p_scaffold.add_argument("ddx_path", help="Path to the local original .DDX file.")
    p_scaffold.add_argument("--out", help="Output JSON path (default: localization/translated/<name>.json).")
    p_scaffold.set_defaults(func=cmd_scaffold)

    p_status = sub.add_parser("status", help="Show translation progress for a translation file (reads only the JSON, no local DDX needed).")
    p_status.add_argument("json_path", help="Path to the translation JSON file.")
    p_status.add_argument("--show-untranslated", action="store_true", help="Print each untranslated entry's stored source text.")
    p_status.set_defaults(func=cmd_status)

    p_build = sub.add_parser("build", help="Merge translations into a localized DDX.")
    p_build.add_argument("ddx_path", help="Path to the local original .DDX file.")
    p_build.add_argument("json_path", help="Path to the translation JSON file.")
    p_build.add_argument("out", help="Output path for the localized .DDX file.")
    p_build.add_argument("--mapping", default=str(_DEFAULT_MAPPING), help="Path to zh_mapping.json.")
    p_build.set_defaults(func=cmd_build)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
