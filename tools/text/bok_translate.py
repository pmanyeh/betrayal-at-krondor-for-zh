#!/usr/bin/env python3
"""
Betrayal at Krondor -- BOK Book Translation Pipeline (Phase 7)

Mirrors the DDX pipeline (`ddx_translate.py`). Canonical translation files
under `localization/translated/BOK_<CHAPTER>.json` store the
id/source/translation/status/notes/tokens for each text run in a chapter
book, so a translation can be reviewed side by side with its English
source directly in the tracked file. Because the source text is committed,
`scaffold` and `build` both re-read the local BOK and warn loudly on any
source-text drift.

Pipeline: original BOK (local, gitignored, via bok_extract_pristine.py)
          -> scaffold  -> localization/translated/BOK_<CHAPTER>.json
          -> (human/agent fills in "translation" + "status")
          -> build     -> localized BOK (build output, gitignored)
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bok_extract import extract_bok_data  # noqa: E402
from bok_rebuild_common import build_bok_file, entry_id, iter_runs  # noqa: E402
from ddx_rebuild_common import extract_tokens  # noqa: E402

_DEFAULT_MAPPING = Path(__file__).resolve().parents[2] / "localization" / "generated" / "zh_mapping.json"


def _preview(source: str, width: int = 70) -> str:
    return "".join(c if 0x20 <= ord(c) < 0x7F else f"\\x{ord(c):02x}" for c in source[:width])


def cmd_scaffold(args: argparse.Namespace) -> None:
    bok_path = Path(args.bok_path)
    bok_name = bok_path.name
    extracted = extract_bok_data(bok_path.read_bytes())

    out_path = Path(args.out) if args.out else Path("localization/translated") / ("BOK_" + bok_path.stem + ".json")

    existing: dict[str, dict[str, Any]] = {}
    if out_path.exists():
        for e in json.loads(out_path.read_text(encoding="utf-8")).get("entries", []):
            existing[e["id"]] = e

    new_entries = []
    seen_ids: set[str] = set()
    drifted = []
    for page_index, run_index, item in iter_runs(extracted):
        eid = entry_id(bok_name, page_index, run_index)
        seen_ids.add(eid)
        prior = existing.get(eid)
        if prior is not None and prior.get("source") != item["text"]:
            drifted.append(eid)
        new_entries.append({
            "id": eid,
            "page": page_index,
            "run": run_index,
            "source": item["text"],
            "tokens": extract_tokens(item["text"]),
            "translation": prior["translation"] if prior else "",
            "status": prior["status"] if prior else "untranslated",
            "notes": prior["notes"] if prior else "",
        })

    stale = set(existing) - seen_ids
    if stale:
        print(f"warning: {len(stale)} previously-scaffolded id(s) no longer present in {bok_name}: "
              f"{sorted(stale)[:10]}", file=sys.stderr)
    if drifted:
        print(f"warning: {len(drifted)} id(s) have a DIFFERENT source text than what's already on file: "
              f"{drifted[:10]}", file=sys.stderr)

    out_data = {
        "format": "BAK_ZH_TRANSLATION",
        "version": 1,
        "source_bok": bok_name,
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
    print(f"{data.get('source_bok', '?')}: {len(entries)} entries")
    for status, count in sorted(by_status.items()):
        print(f"  {status}: {count}")
    if args.show_untranslated:
        print("\nUntranslated:")
        for e in entries:
            if e["status"] == "untranslated":
                print(f"  {e['id']}: {_preview(e.get('source', ''))}")


def cmd_build(args: argparse.Namespace) -> None:
    out_path = Path(args.out)
    stats = build_bok_file(Path(args.bok_path), Path(args.json_path), out_path, Path(args.mapping))
    print(f"Built {out_path}: {stats['applied']} run(s) translated, "
          f"{stats['skipped_untranslated']} marked-but-empty skipped, "
          f"{stats['skipped_token_mismatch']} token-mismatch fallback(s), "
          f"{stats['skipped_source_drift']} source-drift fallback(s)")


def main() -> None:
    parser = argparse.ArgumentParser(description="Betrayal at Krondor BOK translation pipeline.")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("scaffold", help="Create/update a translation file from a local BOK.")
    p.add_argument("bok_path", help="Path to the local original .BOK file.")
    p.add_argument("--out", help="Output JSON path (default: localization/translated/BOK_<name>.json).")
    p.set_defaults(func=cmd_scaffold)

    p = sub.add_parser("status", help="Show translation progress (reads only the JSON).")
    p.add_argument("json_path")
    p.add_argument("--show-untranslated", action="store_true")
    p.set_defaults(func=cmd_status)

    p = sub.add_parser("build", help="Merge translations into a localized BOK.")
    p.add_argument("bok_path")
    p.add_argument("json_path")
    p.add_argument("out")
    p.add_argument("--mapping", default=str(_DEFAULT_MAPPING))
    p.set_defaults(func=cmd_build)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
