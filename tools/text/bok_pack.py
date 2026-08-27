#!/usr/bin/env python3
"""
Betrayal at Krondor -- BOK Book Packer (Phase 7)

Serializes the structured dict produced by `bok_extract.extract_bok_data`
back into a `.BOK` file. Unlike the DDX packer -- which must preserve every
record's byte length because opcodes address by absolute offset -- BOK
navigation is entirely by logical page number (`wPageNumber`), so the
localized text stream is free to change length: only the blob-relative
page-offset table and the u32 file-size header are recomputed here.
"""

from __future__ import annotations

import argparse
import json
import struct
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bok_extract import _PAGE_HDR, _PAGE_HDR_TOTAL, extract_bok_data  # noqa: E402

_CTRL_TAG = {"layout": 0xF1, "style": 0xF4, "hook": 0xF3, "end": 0xF0}
_CTRL_PAYLOAD = {"layout": 16, "style": 10, "hook": 2, "end": 0}


def _serialize_stream(stream: list[dict[str, Any]]) -> bytes:
    out = bytearray()
    saw_end = False
    for item in stream:
        kind = item["kind"]
        if kind == "text":
            out.extend(item["text"].encode("latin1"))
            continue
        if kind not in _CTRL_TAG:
            raise ValueError(f"unknown stream item kind {kind!r}")
        out.append(_CTRL_TAG[kind])
        want = _CTRL_PAYLOAD[kind]
        if want:
            payload = bytes.fromhex(item["hex"])
            if len(payload) != want:
                raise ValueError(f"{kind} block payload is {len(payload)} bytes, expected {want}")
            out.extend(payload)
        if kind == "end":
            saw_end = True
            break
    if not saw_end:
        raise ValueError("stream has no 'end' item")
    return bytes(out)


def _serialize_page(page: dict[str, Any]) -> bytes:
    reserved = bytes.fromhex(page["pReserved_hex"])
    if len(reserved) != 30:
        raise ValueError("pReserved must be 30 bytes")
    rects = page["reserved_rects"]
    images = page["images"]
    if len(rects) != page["wReservedCount"]:
        raise ValueError("wReservedCount does not match reserved_rects length")
    if len(images) != page["wImageCount"]:
        raise ValueError("wImageCount does not match images length")

    out = bytearray()
    out.extend(_PAGE_HDR.pack(
        *page["rect"],
        page["wDisplayNumber"],
        page["wPageNumber"],
        page["wPrevPageNumber"],
        page["wNextPageNumber"],
        page["wPagePointer"],
        page["w_pad12"],
        page["wImageCount"],
        page["wReservedCount"],
        page["wShowPageNumber"],
    ))
    out.extend(reserved)
    assert len(out) == _PAGE_HDR_TOTAL
    for r in rects:
        out.extend(struct.pack("<hhhh", *r))
    for im in images:
        out.extend(struct.pack("<hhHH", *im))
    out.extend(_serialize_stream(page["stream"]))
    return bytes(out)


def pack_bok_data(extracted: dict[str, Any]) -> bytes:
    pages = extracted["pages"]
    n = len(pages)
    if n != extracted["page_count"]:
        raise ValueError("page_count does not match number of pages")

    page_blobs = [_serialize_page(pg) for pg in pages]
    table_size = 2 + n * 4
    offsets = []
    cursor = table_size
    for pb in page_blobs:
        offsets.append(cursor)
        cursor += len(pb)

    blob = bytearray()
    blob.extend(struct.pack("<h", n))
    for off in offsets:
        blob.extend(struct.pack("<I", off))
    for pb in page_blobs:
        blob.extend(pb)

    return struct.pack("<I", len(blob)) + bytes(blob)


def validate_bok_data(payload: bytes, label: str = "<bok>") -> None:
    """Round-trip check: a freshly packed file must re-parse cleanly."""
    try:
        extract_bok_data(payload)
    except ValueError as exc:
        raise ValueError(f"{label}: packed BOK failed re-parse: {exc}") from exc


def main() -> None:
    parser = argparse.ArgumentParser(description="Pack a Betrayal at Krondor .BOK JSON back to binary.")
    parser.add_argument("input_json", type=Path, help="Path to input .json (from bok_extract)")
    parser.add_argument("output_bok", type=Path, help="Path to output .BOK file")
    args = parser.parse_args()

    extracted = json.loads(args.input_json.read_text(encoding="utf-8"))
    packed = pack_bok_data(extracted)
    validate_bok_data(packed, label=str(args.output_bok))
    args.output_bok.write_bytes(packed)
    print(f"Packed {len(packed)} bytes to {args.output_bok}", file=sys.stderr)


if __name__ == "__main__":
    main()
