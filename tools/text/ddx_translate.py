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
from ddx_rebuild_common import build_ddx_file, extract_tokens  # noqa: E402

_DEFAULT_MAPPING = Path(__file__).resolve().parents[2] / "localization" / "generated" / "zh_mapping.json"


def _entry_id(ddx_name: str, rec_index: int) -> str:
    return f"{ddx_name}#{rec_index}"


def _preview(source: str, width: int = 70) -> str:
    return "".join(
        char if 0x20 <= ord(char) < 0x7F else f"\\x{ord(char):02x}"
        for char in source[:width]
    )


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
    out_path = Path(args.out)
    stats = build_ddx_file(Path(args.ddx_path), Path(args.json_path), out_path, Path(args.mapping))
    print(f"Built {out_path}: {stats['applied']} record(s) translated, "
          f"{stats['skipped_untranslated']} marked-but-empty skipped, "
          f"{stats['skipped_token_mismatch']} token-mismatch fallback(s), "
          f"{stats['skipped_source_drift']} source-drift fallback(s)")


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
