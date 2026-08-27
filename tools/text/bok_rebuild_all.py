#!/usr/bin/env python3
"""Safely rebuild every translated Cxx.BOK from one pristine source tree.

Mirror of ddx_rebuild_all.py: all sources are checked before any output is
replaced; outputs are built and re-parsed in a temporary sibling directory,
then promoted only after the whole batch succeeds.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path

try:  # Direct script execution
    from bok_extract import extract_bok_data
    from bok_rebuild_common import build_bok_file
except ModuleNotFoundError:  # ``from tools.text...`` in unit tests
    from tools.text.bok_extract import extract_bok_data
    from tools.text.bok_rebuild_common import build_bok_file


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _translation_inputs(translations_dir: Path) -> list[tuple[Path, str]]:
    inputs: list[tuple[Path, str]] = []
    for json_path in sorted(translations_dir.glob("BOK_C*.json")):
        data = json.loads(json_path.read_text(encoding="utf-8"))
        source_bok = data.get("source_bok")
        if not isinstance(source_bok, str) or Path(source_bok).name != source_bok:
            raise ValueError(f"{json_path}: invalid or missing source_bok")
        if Path(source_bok).suffix.upper() != ".BOK":
            raise ValueError(f"{json_path}: source_bok must end in .BOK")
        inputs.append((json_path, source_bok))
    if not inputs:
        raise ValueError(f"no BOK_C*.json files found in {translations_dir}")
    return inputs


def rebuild_all(
    source_dir: Path,
    translations_dir: Path,
    output_dir: Path,
    mapping: Path,
    manifest: Path | None = None,
) -> list[dict[str, object]]:
    source_dir = source_dir.resolve()
    translations_dir = translations_dir.resolve()
    output_dir = output_dir.resolve()
    mapping = mapping.resolve()

    if source_dir == output_dir:
        raise ValueError("source-dir and output-dir must be different directories")
    for label, path in (("source", source_dir), ("translations", translations_dir)):
        if not path.is_dir():
            raise ValueError(f"{label} directory does not exist: {path}")
    if not mapping.is_file():
        raise ValueError(f"mapping file does not exist: {mapping}")

    inputs = _translation_inputs(translations_dir)
    source_paths = [(jp, source_dir / name) for jp, name in inputs]
    missing = [str(sp) for _, sp in source_paths if not sp.is_file()]
    if missing:
        raise ValueError("refusing partial rebuild; missing pristine source BOK file(s):\n  - " + "\n  - ".join(missing))

    # Validate every source parses before touching output.
    for _, sp in source_paths:
        extract_bok_data(sp.read_bytes())

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    temp_dir = Path(tempfile.mkdtemp(prefix=".bok_rebuild_", dir=output_dir.parent))
    results: list[dict[str, object]] = []
    try:
        for json_path, source_path in source_paths:
            built = temp_dir / source_path.name
            stats = build_bok_file(source_path, json_path, built, mapping)
            extract_bok_data(built.read_bytes())  # re-parse the promoted artifact
            results.append({
                "source": source_path.name,
                "translation": str(json_path),
                "output": source_path.name,
                "source_sha256": _sha256(source_path),
                "output_sha256": _sha256(built),
                **stats,
            })

        output_dir.mkdir(parents=True, exist_ok=True)
        for result in results:
            name = str(result["output"])
            (temp_dir / name).replace(output_dir / name)

        if manifest is not None:
            manifest.parent.mkdir(parents=True, exist_ok=True)
            manifest.write_text(
                json.dumps({"format": "BAK_ZH_BOK_BUILD", "version": 1, "files": results}, indent=2),
                encoding="utf-8",
            )
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
    return results


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(
        description="Validate and rebuild every BOK_C*.json from a complete pristine BOK directory."
    )
    parser.add_argument("--source-dir", type=Path, default=repo_root / "scratchpad" / "pristine_bok")
    parser.add_argument("--translations-dir", type=Path, default=repo_root / "localization" / "translated")
    parser.add_argument("--output-dir", type=Path, default=repo_root / "dist" / "test_v100_zh")
    parser.add_argument("--mapping", type=Path, default=repo_root / "localization" / "generated" / "zh_mapping.json")
    parser.add_argument("--manifest", type=Path, help="Optional JSON manifest written after a successful promotion.")
    args = parser.parse_args()

    try:
        results = rebuild_all(args.source_dir, args.translations_dir, args.output_dir, args.mapping, args.manifest)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    applied = sum(int(r["applied"]) for r in results)
    mism = sum(int(r["skipped_token_mismatch"]) for r in results)
    drift = sum(int(r["skipped_source_drift"]) for r in results)
    print(f"Rebuilt and validated {len(results)} BOK file(s); {applied} run(s) applied, "
          f"{mism} token-mismatch fallback(s), {drift} source-drift fallback(s).")


if __name__ == "__main__":
    main()
