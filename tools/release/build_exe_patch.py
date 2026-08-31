"""Developer-side tool: produce a BSDIFF4 binary patch that turns a legally
owned, unmodified v1.00 KRONDOR.EXE into this project's translated build.

We never distribute the compiled translated EXE itself -- it is a rebuild of
the original commercial game binary from reconstructed source, and the
upstream recompilation project's LICENSE explicitly does not extend to that
third-party material. Only a binary diff is published; end users apply it
locally to their own copy via `installer.py`.

Requires `bsdiff4` (`pip install bsdiff4`) -- developer-only dependency, not
needed by the end-user installer (see `bspatch_apply.py`).

Usage:
    python tools/release/build_exe_patch.py \\
        --original betrayal-at-krondor/krondor.exe \\
        --translated dist/test_v100_zh/krondor.exe \\
        --out-dir dist/release_v100_zh/exe_patch
"""

from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

try:
    import bsdiff4
except ImportError as exc:  # pragma: no cover
    raise SystemExit("This dev tool needs bsdiff4: pip install bsdiff4") from exc

# From docs/baseline/version-evidence.md section 3.1 -- the only original
# release this project has been built and verified against so far.
BASELINE_VERSION_LABEL = "v1.00 Floppy (1993-06-16)"
BASELINE_SIZE = 453_904
BASELINE_SHA256 = "c943fd895a570224813c767d47acf44299c0aff972f1ea5f743aef303ebdd7fe"

PATCH_FILENAME = "krondor_v100_zh.bspatch"
MANIFEST_FILENAME = "manifest.json"


def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def build(original_path: Path, translated_path: Path, out_dir: Path) -> None:
    original = original_path.read_bytes()
    original_hash = sha256_of(original)
    if len(original) != BASELINE_SIZE or original_hash != BASELINE_SHA256:
        raise SystemExit(
            f"拒絕產生補丁：{original_path} 不是已知的 {BASELINE_VERSION_LABEL} 基準版本\n"
            f"  預期：{BASELINE_SIZE} bytes, sha256 {BASELINE_SHA256}\n"
            f"  實際：{len(original)} bytes, sha256 {original_hash}"
        )

    translated = translated_path.read_bytes()
    translated_hash = sha256_of(translated)

    patch_bytes = bsdiff4.diff(original, translated)

    out_dir.mkdir(parents=True, exist_ok=True)
    patch_path = out_dir / PATCH_FILENAME
    patch_path.write_bytes(patch_bytes)

    manifest = {
        "format": "bak-zh-exe-patch",
        "version": 1,
        "built_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "baseline": {
            "filename": "KRONDOR.EXE",
            "version_label": BASELINE_VERSION_LABEL,
            "size": len(original),
            "sha256": original_hash,
        },
        "target": {
            "filename": "KRONDOR.EXE",
            "size": len(translated),
            "sha256": translated_hash,
        },
        "patch_file": PATCH_FILENAME,
        "patch_sha256": sha256_of(patch_bytes),
        "patch_size": len(patch_bytes),
    }
    (out_dir / MANIFEST_FILENAME).write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    print(f"OK: {patch_path} ({len(patch_bytes)} bytes)")
    print(f"    baseline {BASELINE_VERSION_LABEL}: {len(original)} bytes, sha256 {original_hash}")
    print(f"    target:                          {len(translated)} bytes, sha256 {translated_hash}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--original", type=Path, default=Path("betrayal-at-krondor/krondor.exe"))
    parser.add_argument("--translated", type=Path, default=Path("dist/test_v100_zh/krondor.exe"))
    parser.add_argument("--out-dir", type=Path, default=Path("dist/release_v100_zh/exe_patch"))
    args = parser.parse_args()
    build(args.original, args.translated, args.out_dir)


if __name__ == "__main__":
    main()
