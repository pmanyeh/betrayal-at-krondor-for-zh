#!/usr/bin/env python3
"""Structural validation for Betrayal at Krondor DDX dialog files.

The game treats DDX offsets as trusted pointers.  A syntactically readable
file can therefore still corrupt memory if a directory entry or a choice
target lands in the middle of a record.  This validator makes those errors
build-time failures.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:  # Direct script execution
    from ddx_extract import extract_ddx_data
except ModuleNotFoundError:  # ``from tools.text...`` in unit tests
    from tools.text.ddx_extract import extract_ddx_data


class DdxValidationError(ValueError):
    """A DDX file has an invalid record boundary or pointer."""


def validate_ddx_data(payload: bytes, *, label: str = "DDX") -> dict[str, int]:
    """Validate record boundaries plus all known DDX record pointers.

    Returns a small summary on success.  Raises :class:`DdxValidationError`
    with every discovered structural error on failure.
    """
    try:
        data = extract_ddx_data(payload)
    except ValueError as exc:
        raise DdxValidationError(f"{label}: cannot parse DDX: {exc}") from exc

    records = data["records"]
    offsets = {record["orig_offset"] for record in records}
    errors: list[str] = []

    if len(offsets) != len(records):
        errors.append("duplicate record offsets")

    for index, (node_id, target) in enumerate(data["dir_entries"]):
        if target not in offsets:
            errors.append(
                f"directory entry {index} (node {node_id}) points to "
                f"{target:#x}, not a record boundary"
            )

    local_choice_targets = 0
    external_choice_targets = 0
    for record in records:
        for choice_index, choice in enumerate(record["choices"]):
            target = choice["nA3"] | (choice["nA4"] << 16)
            # A zero target is the format's null/no-child sentinel.
            if target == 0:
                continue
            # Bit 31 marks a global/keyed target rather than an offset into
            # this DDX file.  These targets deliberately do not refer to a
            # local record boundary (for example 0x800000c4).
            if target & 0x80000000:
                external_choice_targets += 1
                continue
            local_choice_targets += 1
            if target not in offsets:
                errors.append(
                    f"record {record['rec_index']} at {record['orig_offset']:#x}, "
                    f"choice {choice_index} points to {target:#x}, "
                    "not a record boundary"
                )

    if errors:
        details = "\n  - ".join(errors)
        raise DdxValidationError(f"{label}: structural validation failed:\n  - {details}")

    return {
        "records": len(records),
        "directory_entries": len(data["dir_entries"]),
        "local_choice_targets": local_choice_targets,
        "external_choice_targets": external_choice_targets,
    }


def validate_ddx_file(path: Path) -> dict[str, int]:
    """Read and validate one DDX file."""
    return validate_ddx_data(path.read_bytes(), label=str(path))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Validate DDX record boundaries, directory targets, and choice targets."
    )
    parser.add_argument("ddx", nargs="+", type=Path, help="DDX file(s) to validate")
    args = parser.parse_args()

    failures = 0
    for path in args.ddx:
        try:
            summary = validate_ddx_file(path)
        except (OSError, DdxValidationError) as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            failures += 1
            continue
        print(
            f"OK {path}: {summary['records']} records, "
            f"{summary['directory_entries']} directory entries, "
            f"{summary['local_choice_targets']} local choice targets, "
            f"{summary['external_choice_targets']} global/keyed targets"
        )

    if failures:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
