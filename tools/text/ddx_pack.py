#!/usr/bin/env python3
"""
Betrayal at Krondor — DDX Dialog Packer
Packs structured JSON back into binary DIAL_Zxx.DDX files.
Reconstructs directory table, updates all record offsets and internal choice/opcode pointers.
"""

from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path
from typing import Any

# struct DDXRecord {
#     unsigned char bStyle;        // 1 byte
#     unsigned short wSpeaker_id;  // 2 bytes
#     unsigned short wFlags;       // 2 bytes
#     unsigned char bCnt1;         // 1 byte
#     unsigned char bCnt2;         // 1 byte
#     unsigned short wBody_len;    // 2 bytes
# }
_DDX_RECORD_HDR = struct.Struct("<BHHBBH")


def pack_ddx_data(data: dict[str, Any], use_raw_hex: bool = False) -> bytes:
    """Serializes a structured dictionary into a binary DDX payload."""
    records = data.get("records", [])
    dir_entries_in = data.get("dir_entries", [])
    dir_count = len(dir_entries_in)

    # Initial directory size
    dir_size = 2 + dir_count * 8

    # Pass 1: Compute lengths and new offsets for each record
    orig_off_to_new_off: dict[int, int] = {}
    record_lengths: list[int] = []
    record_bodies: list[bytes] = []

    current_offset = dir_size
    for rec in records:
        orig_off = rec.get("orig_offset", 0)
        orig_off_to_new_off[orig_off] = current_offset

        choices = rec.get("choices", [])
        opcodes = rec.get("opcodes", [])
        cnt1 = len(choices)
        cnt2 = len(opcodes)

        if use_raw_hex and "raw_hex" in rec:
            body_bytes = bytes.fromhex(rec["raw_hex"])
        else:
            text_str = rec.get("text", "")
            body_bytes = text_str.encode("latin1")

        record_bodies.append(body_bytes)
        rec_total_len = _DDX_RECORD_HDR.size + (cnt1 + cnt2) * 10 + len(body_bytes)
        record_lengths.append(rec_total_len)
        current_offset += rec_total_len

    # Pass 2: Reconstruct new directory entries
    new_dir_entries: list[tuple[int, int]] = []
    for node_id, orig_off in dir_entries_in:
        new_off = orig_off_to_new_off.get(orig_off, orig_off)
        new_dir_entries.append((node_id, new_off))

    # Pass 3: Build record binary blobs.  A choice's nA3/nA4 words are one
    # 32-bit dwTarget_key.  Offset-based child choices can therefore point
    # beyond 64 KiB and must be remapped as a single value when translated
    # text changes record positions.
    #
    # DdxOp opcode 0x10 likewise stores a 32-bit dialog return target in
    # nA1/nA2.  dialog_play_record() pushes that value on keyStack and loads
    # it after a child dialog (including Ask About) returns.  Leaving this
    # operand at its pristine offset makes translated, variable-length DDX
    # files jump into the middle of a record.  Other opcode operands are not
    # record pointers and must remain byte-for-byte unchanged.
    body_chunks: list[bytes] = []
    for i, rec in enumerate(records):
        style = rec["style"]
        speaker = rec["speaker_id"]
        flags = rec["flags"]
        choices = rec.get("choices", [])
        opcodes = rec.get("opcodes", [])
        body_bytes = record_bodies[i]
        body_len = len(body_bytes)
        cnt1 = len(choices)
        cnt2 = len(opcodes)

        # Pack choices (cnt1 * 10 bytes)
        choices_bin = bytearray()
        for ch in choices:
            target_key = ch["nA3"] | (ch["nA4"] << 16)
            target_key = orig_off_to_new_off.get(target_key, target_key)
            choices_bin += struct.pack(
                "<HHHHH",
                ch["wCond"],
                ch["nA1"],
                ch["nA2"],
                target_key & 0xFFFF,
                (target_key >> 16) & 0xFFFF,
            )

        # Pack opcodes (cnt2 * 10 bytes)
        opcodes_bin = bytearray()
        for op in opcodes:
            nA1 = op["nA1"]
            nA2 = op["nA2"]
            if op["wOp"] == 0x10:
                return_key = nA1 | (nA2 << 16)
                return_key = orig_off_to_new_off.get(return_key, return_key)
                nA1 = return_key & 0xFFFF
                nA2 = (return_key >> 16) & 0xFFFF
            opcodes_bin += struct.pack(
                "<HHHHH", op["wOp"], nA1, nA2, op["nA3"], op["nA4"]
            )

        hdr_bin = _DDX_RECORD_HDR.pack(style, speaker, flags, cnt1, cnt2, body_len)
        body_chunks.append(hdr_bin + choices_bin + opcodes_bin + body_bytes)

    # Assemble final binary
    output = bytearray()
    output += struct.pack("<H", dir_count)
    for node_id, file_off in new_dir_entries:
        output += struct.pack("<II", node_id, file_off)

    for chunk in body_chunks:
        output += chunk

    return bytes(output)


def main() -> None:
    parser = argparse.ArgumentParser(description="Pack JSON dialogs back into DDX binary.")
    parser.add_argument("input_json", type=Path, help="Path to input .json file")
    parser.add_argument("output_ddx", type=Path, nargs="?", help="Path to output .ddx file (optional)")
    parser.add_argument("--raw-hex", action="store_true", help="Use raw_hex field if present (exact byte match)")
    args = parser.parse_args()

    data = json.loads(args.input_json.read_text(encoding="utf-8"))
    packed = pack_ddx_data(data, use_raw_hex=args.raw_hex)

    out_path = args.output_ddx or args.input_json.with_suffix(".DDX")
    out_path.write_bytes(packed)
    print(f"Packed {len(data.get('records', []))} records ({len(packed)} bytes) to {out_path}")


if __name__ == "__main__":
    main()
