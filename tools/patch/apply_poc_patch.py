#!/usr/bin/env python3
"""
Betrayal at Krondor — Phase 4 POC Patch Generator
Applies the POC Traditional Chinese test sentence to Chapter 1 dialog record 100009.
"""

from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path
from typing import Any

# Ensure project root is on sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from tools.font.build_font import encode_string
from tools.text.ddx_extract import extract_ddx_data
from tools.text.ddx_pack import pack_ddx_data


def generate_poc_patch(
    arc_path: Path,
    rmf_path: Path,
    mapping_path: Path,
    output_dir: Path,
) -> tuple[Path, dict[str, Any]]:
    """Extracts DIAL_Z01.DDX, patches record 100009 with Chinese text, and saves patched DDX."""
    mapping_data = json.loads(mapping_path.read_text(encoding="utf-8"))
    char_to_id = mapping_data["char_to_id"]

    # Extract original DIAL_Z01.DDX from archive
    rmf_data = rmf_path.read_bytes()
    (count,) = struct.unpack_from("<H", rmf_data, 19)
    table = 21

    ddx_bytes = None
    with arc_path.open("rb") as f:
        for i in range(count):
            hkey, off = struct.unpack_from("<II", rmf_data, table + i * 8)
            f.seek(off)
            entry_hdr = f.read(17)
            name = entry_hdr[:13].split(b"\0", 1)[0].decode("ascii")
            (size,) = struct.unpack_from("<I", entry_hdr, 13)
            if name.upper() == "DIAL_Z01.DDX":
                ddx_bytes = f.read(size)
                break

    if ddx_bytes is None:
        raise FileNotFoundError("DIAL_Z01.DDX not found in krondor.001")

    extracted = extract_ddx_data(ddx_bytes)

    # Locate Record 100009
    target_rec = None
    for rec in extracted["records"]:
        if rec.get("node_id") == 100009:
            target_rec = rec
            break

    if target_rec is None:
        raise ValueError("Record 100009 not found in DIAL_Z01.DDX")

    # POC Test Sentence:
    # \tMist floated in the pass.\n\t歐文：我們在哪裡？\n\t"This road branches a little further..."
    zh_sentence = "歐文：我們在哪裡？"
    encoded_zh = encode_string(zh_sentence, char_to_id).decode("latin1")
    new_text = (
        f'\tMist floated in the pass.\n\t{encoded_zh}\n\t"This road branches a little further south, one way to '
        f'the North road and the other toward Sethanon. Which way should we go?"\x00'
    )

    target_rec["text"] = new_text
    # Clear raw_hex so packer uses updated text
    target_rec.pop("raw_hex", None)

    # Pack to new DDX binary
    patched_ddx = pack_ddx_data(extracted)

    output_dir.mkdir(parents=True, exist_ok=True)
    out_file = output_dir / "DIAL_Z01.DDX"
    out_file.write_bytes(patched_ddx)

    meta = {
        "target_file": "DIAL_Z01.DDX",
        "target_node_id": 100009,
        "original_size": len(ddx_bytes),
        "patched_size": len(patched_ddx),
        "zh_sentence": zh_sentence,
        "encoded_hex": encode_string(zh_sentence, char_to_id).hex(),
    }

    return out_file, meta


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate Phase 4 POC Patched DDX.")
    parser.add_argument(
        "--arc",
        type=Path,
        default=Path(r"d:\git\betrayal-at-krondor-for-zh\betrayal-at-krondor\krondor.001"),
        help="Path to krondor.001",
    )
    parser.add_argument(
        "--rmf",
        type=Path,
        default=Path(r"d:\git\betrayal-at-krondor-for-zh\betrayal-at-krondor\krondor.rmf"),
        help="Path to krondor.rmf",
    )
    parser.add_argument(
        "--mapping",
        type=Path,
        default=Path(r"d:\git\betrayal-at-krondor-for-zh\localization\generated\zh_mapping.json"),
        help="Path to zh_mapping.json",
    )
    parser.add_argument(
        "--outdir",
        type=Path,
        default=Path(r"d:\git\betrayal-at-krondor-for-zh\localization\generated"),
        help="Output directory",
    )
    args = parser.parse_args()

    out_file, meta = generate_poc_patch(args.arc, args.rmf, args.mapping, args.outdir)
    print(f"Generated patched DDX -> {out_file} ({meta['patched_size']} bytes)")
    print(f"Patched Record {meta['target_node_id']} with: {meta['zh_sentence']}")
    print(f"Encoded Hex: {meta['encoded_hex']}")


if __name__ == "__main__":
    main()
