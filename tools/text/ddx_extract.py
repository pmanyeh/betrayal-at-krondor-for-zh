#!/usr/bin/env python3
"""
Betrayal at Krondor — DDX Dialog Extractor
Extracts DIAL_Zxx.DDX binary dialog files into structured UTF-8 JSON.
Preserves all record keys, child/sub-records, choice descriptors, opcodes, titles, and text.
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
#     unsigned char bCnt1;         // 1 byte (number of DdxChoice entries)
#     unsigned char bCnt2;         // 1 byte (number of DdxOp entries)
#     unsigned short wBody_len;    // 2 bytes (length of text body)
# }
_DDX_RECORD_HDR = struct.Struct("<BHHBBH")


def extract_ddx_data(payload: bytes) -> dict[str, Any]:
    """Parses DDX binary payload into a structured Python dictionary."""
    if len(payload) < 2:
        raise ValueError("DDX payload too small (less than 2 bytes)")

    (dir_count,) = struct.unpack_from("<H", payload, 0)
    pos = 2

    # Map file_offset -> list of node_ids (or single node_id)
    dir_entries: list[tuple[int, int]] = []
    dir_offset_to_key: dict[int, int] = {}
    for _ in range(dir_count):
        if pos + 8 > len(payload):
            raise ValueError("Corrupt DDX directory table (unexpected EOF)")
        node_id, file_off = struct.unpack_from("<II", payload, pos)
        pos += 8
        dir_entries.append((node_id, file_off))
        dir_offset_to_key[file_off] = node_id

    cur_offset = 2 + dir_count * 8
    records: list[dict[str, Any]] = []
    record_index = 0

    while cur_offset < len(payload):
        rec_start = cur_offset
        if rec_start + _DDX_RECORD_HDR.size > len(payload):
            raise ValueError(f"Record header at {rec_start:#x} out of bounds")

        style, speaker, flags, cnt1, cnt2, body_len = _DDX_RECORD_HDR.unpack_from(payload, rec_start)
        r_pos = rec_start + _DDX_RECORD_HDR.size

        # Parse Choices: cnt1 * 10 bytes
        choices: list[dict[str, int]] = []
        for _ in range(cnt1):
            if r_pos + 10 > len(payload):
                raise ValueError(f"Record at {rec_start:#x} choices truncated")
            wCond, nA1, nA2, nA3, nA4 = struct.unpack_from("<HHHHH", payload, r_pos)
            choices.append({
                "wCond": wCond,
                "nA1": nA1,
                "nA2": nA2,
                "nA3": nA3,
                "nA4": nA4,
            })
            r_pos += 10

        # Parse Opcodes: cnt2 * 10 bytes
        opcodes: list[dict[str, int]] = []
        for _ in range(cnt2):
            if r_pos + 10 > len(payload):
                raise ValueError(f"Record at {rec_start:#x} opcodes truncated")
            wOp, nA1, nA2, nA3, nA4 = struct.unpack_from("<HHHHH", payload, r_pos)
            opcodes.append({
                "wOp": wOp,
                "nA1": nA1,
                "nA2": nA2,
                "nA3": nA3,
                "nA4": nA4,
            })
            r_pos += 10

        # Parse text body: body_len bytes
        body_bytes = payload[r_pos : r_pos + body_len]
        if len(body_bytes) < body_len:
            raise ValueError(f"Record at {rec_start:#x} text body truncated")

        try:
            body_text = body_bytes.decode("latin1")
        except Exception:
            body_text = body_bytes.decode("latin1", errors="replace")

        node_id = dir_offset_to_key.get(rec_start, None)

        records.append({
            "rec_index": record_index,
            "orig_offset": rec_start,
            "node_id": node_id,  # None if sub-record / child record
            "style": style,
            "speaker_id": speaker,
            "flags": flags,
            "choices": choices,
            "opcodes": opcodes,
            "text": body_text,
            "raw_hex": body_bytes.hex(),
        })

        cur_offset = r_pos + body_len
        record_index += 1

    return {
        "format": "BAK_DDX",
        "version": 1,
        "dir_entries": dir_entries,  # [(node_id, file_off), ...]
        "total_records": len(records),
        "records": records,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract Betrayal at Krondor DDX to JSON.")
    parser.add_argument("input_ddx", type=Path, help="Path to input .DDX file")
    parser.add_argument("output_json", type=Path, nargs="?", help="Path to output .json file (optional)")
    args = parser.parse_args()

    data = args.input_ddx.read_bytes()
    extracted = extract_ddx_data(data)

    out_path = args.output_json or args.input_ddx.with_suffix(".json")
    out_path.write_text(json.dumps(extracted, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Extracted {extracted['total_records']} records ({len(extracted['dir_entries'])} keyed) to {out_path}")


if __name__ == "__main__":
    main()
