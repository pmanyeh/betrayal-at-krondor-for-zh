#!/usr/bin/env python3
"""Extract canonical DIAL_*.DDX source files from Krondor's resource archive."""

from __future__ import annotations

import argparse
import struct
import sys
from pathlib import Path


_RMF_TABLE_OFFSET = 21
_RESOURCE_HEADER_SIZE = 17


def extract_pristine_dial_ddx(rmf_path: Path, archive_path: Path, output_dir: Path) -> list[Path]:
    """Copy every original DIAL_*.DDX from an RMF-indexed archive.

    Existing files are accepted only when byte-identical. A mismatch is
    refused so source resources from different game releases cannot be mixed.
    """
    rmf = rmf_path.read_bytes()
    if len(rmf) < _RMF_TABLE_OFFSET:
        raise ValueError(f"RMF file is too small: {rmf_path}")
    (count,) = struct.unpack_from("<H", rmf, 19)
    if len(rmf) < _RMF_TABLE_OFFSET + count * 8:
        raise ValueError(f"RMF directory is truncated: {rmf_path}")

    extracted: list[tuple[str, bytes]] = []
    with archive_path.open("rb") as archive:
        for index in range(count):
            _, offset = struct.unpack_from("<II", rmf, _RMF_TABLE_OFFSET + index * 8)
            archive.seek(offset)
            header = archive.read(_RESOURCE_HEADER_SIZE)
            if len(header) != _RESOURCE_HEADER_SIZE:
                raise ValueError(f"archive entry {index} header is truncated at {offset:#x}")
            name = header[:13].split(b"\0", 1)[0].decode("ascii")
            (size,) = struct.unpack_from("<I", header, 13)
            if not (name.upper().startswith("DIAL_") and name.upper().endswith(".DDX")):
                continue
            payload = archive.read(size)
            if len(payload) != size:
                raise ValueError(f"archive entry {name} body is truncated")
            extracted.append((name, payload))

    if not extracted:
        raise ValueError("no DIAL_*.DDX entries found in the resource archive")
    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []
    for name, payload in extracted:
        path = output_dir / name
        if path.exists() and path.read_bytes() != payload:
            raise ValueError(
                f"refusing to overwrite non-identical pristine source: {path}; "
                "use a separate directory for this game release"
            )
        if not path.exists():
            path.write_bytes(payload)
        paths.append(path)
    return paths


def main() -> None:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(
        description="Extract all original DIAL_*.DDX files without modifying the game installation."
    )
    parser.add_argument("--rmf", type=Path, default=repo_root / "betrayal-at-krondor" / "krondor.rmf")
    parser.add_argument("--archive", type=Path, default=repo_root / "betrayal-at-krondor" / "krondor.001")
    parser.add_argument("--output-dir", type=Path, default=repo_root / "scratchpad" / "pristine")
    args = parser.parse_args()
    try:
        paths = extract_pristine_dial_ddx(args.rmf, args.archive, args.output_dir)
    except (OSError, UnicodeDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    print(f"Verified/extracted {len(paths)} pristine DIAL DDX file(s) to {args.output_dir}")


if __name__ == "__main__":
    main()
