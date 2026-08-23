#!/usr/bin/env python3
"""Safely rebuild every translated DIAL_*.DDX from one pristine source tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
import tempfile
from pathlib import Path

try:  # Direct script execution
    from ddx_rebuild_common import build_ddx_file
    from ddx_validate import DdxValidationError, validate_ddx_file
except ModuleNotFoundError:  # ``from tools.text...`` in unit tests
    from tools.text.ddx_rebuild_common import build_ddx_file
    from tools.text.ddx_validate import DdxValidationError, validate_ddx_file


def _translation_inputs(translations_dir: Path) -> list[tuple[Path, str]]:
    """Return canonical DIAL translation JSON files and their declared source."""
    inputs: list[tuple[Path, str]] = []
    for json_path in sorted(translations_dir.glob("DIAL_*.json")):
        data = json.loads(json_path.read_text(encoding="utf-8"))
        source_ddx = data.get("source_ddx")
        if not isinstance(source_ddx, str) or Path(source_ddx).name != source_ddx:
            raise ValueError(f"{json_path}: invalid or missing source_ddx")
        if Path(source_ddx).suffix.upper() != ".DDX":
            raise ValueError(f"{json_path}: source_ddx must end in .DDX")
        inputs.append((json_path, source_ddx))
    if not inputs:
        raise ValueError(f"no DIAL_*.json files found in {translations_dir}")
    return inputs


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def rebuild_all(
    source_dir: Path,
    translations_dir: Path,
    output_dir: Path,
    mapping: Path,
    manifest: Path | None = None,
) -> list[dict[str, object]]:
    """Build all canonical dialog JSONs as one all-or-nothing batch.

    All sources are checked before any output is replaced.  Outputs are built
    and structurally validated in a temporary sibling directory, then promoted
    only after the complete batch succeeds.
    """
    source_dir = source_dir.resolve()
    translations_dir = translations_dir.resolve()
    output_dir = output_dir.resolve()
    mapping = mapping.resolve()

    if source_dir == output_dir:
        raise ValueError("source-dir and output-dir must be different directories")
    if not source_dir.is_dir():
        raise ValueError(f"source directory does not exist: {source_dir}")
    if not translations_dir.is_dir():
        raise ValueError(f"translations directory does not exist: {translations_dir}")
    if not mapping.is_file():
        raise ValueError(f"mapping file does not exist: {mapping}")

    inputs = _translation_inputs(translations_dir)
    source_paths = [(json_path, source_dir / source_name) for json_path, source_name in inputs]
    missing = [str(source_path) for _, source_path in source_paths if not source_path.is_file()]
    if missing:
        raise ValueError(
            "refusing partial rebuild; missing pristine source DDX file(s):\n  - "
            + "\n  - ".join(missing)
        )

    # Validate every source before creating a build directory or touching output.
    for _, source_path in source_paths:
        validate_ddx_file(source_path)

    output_dir.parent.mkdir(parents=True, exist_ok=True)
    temp_dir = Path(tempfile.mkdtemp(prefix=".ddx_rebuild_", dir=output_dir.parent))
    results: list[dict[str, object]] = []
    try:
        for json_path, source_path in source_paths:
            built_path = temp_dir / source_path.name
            stats = build_ddx_file(source_path, json_path, built_path, mapping)
            validation = validate_ddx_file(built_path)
            results.append({
                "source": source_path.name,
                "translation": str(json_path),
                "output": source_path.name,
                "source_sha256": _sha256(source_path),
                "output_sha256": _sha256(built_path),
                **stats,
                "validation": validation,
            })

        output_dir.mkdir(parents=True, exist_ok=True)
        for result in results:
            name = str(result["output"])
            (temp_dir / name).replace(output_dir / name)

        if manifest is not None:
            manifest.parent.mkdir(parents=True, exist_ok=True)
            manifest.write_text(
                json.dumps({"format": "BAK_ZH_DDX_BUILD", "version": 1, "files": results}, indent=2),
                encoding="utf-8",
            )
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)
    return results


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(
        description="Validate and rebuild every DIAL_*.json from a complete pristine DDX directory."
    )
    parser.add_argument("--source-dir", type=Path, default=repo_root / "scratchpad" / "pristine")
    parser.add_argument("--translations-dir", type=Path, default=repo_root / "localization" / "translated")
    parser.add_argument("--output-dir", type=Path, default=repo_root / "dist" / "test_v100_zh")
    parser.add_argument("--mapping", type=Path, default=repo_root / "localization" / "generated" / "zh_mapping.json")
    parser.add_argument("--manifest", type=Path, help="Optional JSON manifest written after a successful promotion.")
    args = parser.parse_args()

    try:
        results = rebuild_all(
            args.source_dir, args.translations_dir, args.output_dir, args.mapping, args.manifest
        )
    except (OSError, ValueError, DdxValidationError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc

    translated = sum(int(result["applied"]) for result in results)
    print(f"Rebuilt and validated {len(results)} DDX file(s); {translated} translation(s) applied.")


if __name__ == "__main__":
    main()
