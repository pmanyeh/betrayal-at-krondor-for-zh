#!/usr/bin/env python3
"""
Betrayal at Krondor — Message Log (.MLG) format v1 codec / validator.

This is the *offline* half of the message-log feature (see
``docs/research/message-log-format.md`` for the frozen byte layout).  It is a
diagnostic and test tool only: the DOS game never needs Python at runtime.

Responsibilities
----------------
* Encode / decode MLG v1 headers and event records, field by field, little
  endian, with no ``struct``-of-C-struct assumptions.
* Validate a file the way the DOS core does — magic, version, header length,
  header CRC32, committed tail, per-event CRC32, length/offset bounds — and
  report *why* it failed with a distinguishable error code, so tests can assert
  the same reasons the C side returns.
* Produce UTF-8 diagnostics from the in-game BAK-ZH byte encoding, reusing the
  exact mapping the font pipeline generated (``localization/generated/zh_mapping.json``).
* Compute the encoding *mapping fingerprint* that the C header pins as a build
  constant, so a translation rebuild that silently changes the glyph mapping is
  rejected instead of rendering historical text as mojibake.

CLI
---
    python -m tools.text.message_log dump    FILE [--mapping PATH]
    python -m tools.text.message_log verify  FILE
    python -m tools.text.message_log fingerprint [--mapping PATH] [--c-define]
    python -m tools.text.message_log hex2bin  IN.hex OUT.mlg
    python -m tools.text.message_log bin2hex  IN.mlg OUT.hex
"""

from __future__ import annotations

import argparse
import json
import zlib
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, BinaryIO

# --------------------------------------------------------------------------
# Format constants — these MUST stay in lock-step with bak/SRC/DIALOG/MSGLOG.H
# --------------------------------------------------------------------------

MLG_MAGIC = b"BKML"
MLG_FORMAT_VERSION = 1
MLG_HEADER_SIZE = 64
MLG_EVENT_HEAD_SIZE = 52
MLG_EVENT_CRC_SIZE = 4
MLG_EVENT_MIN_RECORD = MLG_EVENT_HEAD_SIZE + MLG_EVENT_CRC_SIZE  # 56

MLG_ENCODING_BAKZH_V1 = 1

MLG_MAX_SPEAKER = 64
MLG_MAX_LOCATION = 64
MLG_MAX_BODY = 512
MLG_MAX_RECORD = MLG_EVENT_HEAD_SIZE + MLG_MAX_SPEAKER + MLG_MAX_LOCATION + MLG_MAX_BODY + 4  # 696
# Hard ceiling on any MLG file. Keeps every offset + record_length sum inside a
# signed 32-bit lseek and leaves three orders of magnitude of headroom before it.
MLG_MAX_FILE = 0x3FFF_FFFF

# --- header flags ---------------------------------------------------------
MLG_HF_SNAPSHOT = 0x0001  # a save-slot snapshot (vs. the live working file)
MLG_HF_HAS_GAP = 0x0002  # timeline contains at least one recording gap
MLG_HF_SEALED = 0x0004  # header was last written by a clean close
MLG_HF_DATA_CRC = 0x0008  # data_crc32 covers [header_length, committed_length)
MLG_HF_GAM_BOUND = 0x0010  # bound_gam_length / bound_gam_crc32 are meaningful

# --- event kinds ----------------------------------------------------------
MLG_KIND_NONE = 0
MLG_KIND_CONV_BEGIN = 1
MLG_KIND_TEXT = 2
MLG_KIND_CHOICE = 3
MLG_KIND_CONV_END = 4
MLG_KIND_GAP = 5
MLG_KIND_SCENE = 6
MLG_KIND_MAX_KNOWN = 6

KIND_NAMES = {
    MLG_KIND_NONE: "NONE",
    MLG_KIND_CONV_BEGIN: "CONV_BEGIN",
    MLG_KIND_TEXT: "TEXT",
    MLG_KIND_CHOICE: "CHOICE",
    MLG_KIND_CONV_END: "CONV_END",
    MLG_KIND_GAP: "GAP",
    MLG_KIND_SCENE: "SCENE",
}

# --- event flags ----------------------------------------------------------
MLG_EV_CONTINUED = 0x0001  # body continues the previous record's body
MLG_EV_MORE = 0x0002  # a further fragment follows this one
MLG_EV_NARRATION = 0x0004  # no speaker (narration / unknown speaker)
MLG_EV_TRUNCATED = 0x0008  # body was cut short by the source buffer

# --- result codes ---------------------------------------------------------
MLG_OK = 0
MLG_E_STATE = -1
MLG_E_PARAM = -2
MLG_E_NOMEM = -3
MLG_E_OPEN = -4
MLG_E_IO = -5
MLG_E_MAGIC = -6
MLG_E_VERSION = -7
MLG_E_HEADER = -8
MLG_E_ENCODING = -9
MLG_E_CRC = -10
MLG_E_TRUNC = -11
MLG_E_RANGE = -12
MLG_E_BINDING = -13
MLG_E_FULL = -14
MLG_E_EMPTY = -15
MLG_E_SUPPRESSED = -16

ERROR_NAMES = {
    MLG_OK: "MLG_OK",
    MLG_E_STATE: "MLG_E_STATE",
    MLG_E_PARAM: "MLG_E_PARAM",
    MLG_E_NOMEM: "MLG_E_NOMEM",
    MLG_E_OPEN: "MLG_E_OPEN",
    MLG_E_IO: "MLG_E_IO",
    MLG_E_MAGIC: "MLG_E_MAGIC",
    MLG_E_VERSION: "MLG_E_VERSION",
    MLG_E_HEADER: "MLG_E_HEADER",
    MLG_E_ENCODING: "MLG_E_ENCODING",
    MLG_E_CRC: "MLG_E_CRC",
    MLG_E_TRUNC: "MLG_E_TRUNC",
    MLG_E_RANGE: "MLG_E_RANGE",
    MLG_E_BINDING: "MLG_E_BINDING",
    MLG_E_FULL: "MLG_E_FULL",
    MLG_E_EMPTY: "MLG_E_EMPTY",
    MLG_E_SUPPRESSED: "MLG_E_SUPPRESSED",
}

# --- states ---------------------------------------------------------------
MLG_STATE_INACTIVE = 0
MLG_STATE_ACTIVE = 1
MLG_STATE_TRANSITION = 2
MLG_STATE_VIEWER = 3
MLG_STATE_FAILED = 4

# BAK-ZH lead/trail byte ranges (mirrors tools/font/build_font.py).
ZH_LEAD_MIN = 0x80
ZH_LEAD_MAX = 0xDF


class MlgError(Exception):
    """A format violation, carrying the same distinguishable code the C core returns."""

    def __init__(self, code: int, message: str, offset: int | None = None):
        self.code = code
        self.offset = offset
        where = "" if offset is None else f" @0x{offset:X}"
        super().__init__(f"{ERROR_NAMES.get(code, code)}{where}: {message}")


# --------------------------------------------------------------------------
# Little-endian primitives (explicit, field-by-field; never a packed C struct)
# --------------------------------------------------------------------------


def put_u16(buf: bytearray, off: int, value: int) -> None:
    if not 0 <= value <= 0xFFFF:
        raise MlgError(MLG_E_RANGE, f"u16 out of range: {value}")
    buf[off] = value & 0xFF
    buf[off + 1] = (value >> 8) & 0xFF


def put_u32(buf: bytearray, off: int, value: int) -> None:
    if not 0 <= value <= 0xFFFF_FFFF:
        raise MlgError(MLG_E_RANGE, f"u32 out of range: {value}")
    buf[off] = value & 0xFF
    buf[off + 1] = (value >> 8) & 0xFF
    buf[off + 2] = (value >> 16) & 0xFF
    buf[off + 3] = (value >> 24) & 0xFF


def get_u16(data: bytes, off: int) -> int:
    return data[off] | (data[off + 1] << 8)


def get_u32(data: bytes, off: int) -> int:
    return data[off] | (data[off + 1] << 8) | (data[off + 2] << 16) | (data[off + 3] << 24)


def crc32(data: bytes, seed: int = 0) -> int:
    """CRC-32/ISO-HDLC (reflected 0xEDB88320, init 0xFFFFFFFF, final xor) — the
    same polynomial and conventions the C core's nibble-table implementation uses."""
    return zlib.crc32(data, seed) & 0xFFFF_FFFF


# --------------------------------------------------------------------------
# MLGTIME — 8 bytes, wall-clock as read from DOS (getdate/gettime)
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class MlgTime:
    year: int = 0
    month: int = 0
    day: int = 0
    hour: int = 0
    minute: int = 0
    second: int = 0
    hundredth: int = 0

    def pack(self) -> bytes:
        buf = bytearray(8)
        put_u16(buf, 0, self.year)
        buf[2] = self.month & 0xFF
        buf[3] = self.day & 0xFF
        buf[4] = self.hour & 0xFF
        buf[5] = self.minute & 0xFF
        buf[6] = self.second & 0xFF
        buf[7] = self.hundredth & 0xFF
        return bytes(buf)

    @staticmethod
    def unpack(data: bytes, off: int = 0) -> MlgTime:
        return MlgTime(
            year=get_u16(data, off),
            month=data[off + 2],
            day=data[off + 3],
            hour=data[off + 4],
            minute=data[off + 5],
            second=data[off + 6],
            hundredth=data[off + 7],
        )

    def __str__(self) -> str:
        return (
            f"{self.year:04d}-{self.month:02d}-{self.day:02d} "
            f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}"
        )


# --------------------------------------------------------------------------
# Header
# --------------------------------------------------------------------------


@dataclass
class MlgHeader:
    format_version: int = MLG_FORMAT_VERSION
    header_length: int = MLG_HEADER_SIZE
    flags: int = 0
    encoding_id: int = MLG_ENCODING_BAKZH_V1
    mapping_fingerprint: int = 0
    bound_gam_length: int = 0
    bound_gam_crc32: int = 0
    committed_length: int = MLG_HEADER_SIZE
    event_count: int = 0
    next_sequence: int = 1
    last_event_offset: int = 0
    data_crc32: int = 0
    created_time: MlgTime = field(default_factory=MlgTime)
    reserved0: int = 0
    reserved1: int = 0
    header_crc32: int = 0

    def pack(self) -> bytes:
        buf = bytearray(MLG_HEADER_SIZE)
        buf[0:4] = MLG_MAGIC
        put_u16(buf, 4, self.format_version)
        put_u16(buf, 6, self.header_length)
        put_u16(buf, 8, self.flags)
        put_u16(buf, 10, self.encoding_id)
        put_u32(buf, 12, self.mapping_fingerprint)
        put_u32(buf, 16, self.bound_gam_length)
        put_u32(buf, 20, self.bound_gam_crc32)
        put_u32(buf, 24, self.committed_length)
        put_u32(buf, 28, self.event_count)
        put_u32(buf, 32, self.next_sequence)
        put_u32(buf, 36, self.last_event_offset)
        put_u32(buf, 40, self.data_crc32)
        buf[44:52] = self.created_time.pack()
        put_u32(buf, 52, self.reserved0)
        put_u32(buf, 56, self.reserved1)
        self.header_crc32 = crc32(bytes(buf[0:60]))
        put_u32(buf, 60, self.header_crc32)
        return bytes(buf)

    @staticmethod
    def unpack(data: bytes, *, check_crc: bool = True) -> MlgHeader:
        if len(data) < MLG_HEADER_SIZE:
            raise MlgError(MLG_E_TRUNC, f"header is {len(data)} bytes, need {MLG_HEADER_SIZE}")
        if data[0:4] != MLG_MAGIC:
            raise MlgError(MLG_E_MAGIC, f"bad magic {data[0:4]!r}")
        version = get_u16(data, 4)
        if version != MLG_FORMAT_VERSION:
            raise MlgError(MLG_E_VERSION, f"unsupported format version {version}")
        header_length = get_u16(data, 6)
        if header_length != MLG_HEADER_SIZE:
            raise MlgError(MLG_E_HEADER, f"header_length {header_length} != {MLG_HEADER_SIZE}")
        hdr = MlgHeader(
            format_version=version,
            header_length=header_length,
            flags=get_u16(data, 8),
            encoding_id=get_u16(data, 10),
            mapping_fingerprint=get_u32(data, 12),
            bound_gam_length=get_u32(data, 16),
            bound_gam_crc32=get_u32(data, 20),
            committed_length=get_u32(data, 24),
            event_count=get_u32(data, 28),
            next_sequence=get_u32(data, 32),
            last_event_offset=get_u32(data, 36),
            data_crc32=get_u32(data, 40),
            created_time=MlgTime.unpack(data, 44),
            reserved0=get_u32(data, 52),
            reserved1=get_u32(data, 56),
            header_crc32=get_u32(data, 60),
        )
        if check_crc:
            want = crc32(bytes(data[0:60]))
            if want != hdr.header_crc32:
                raise MlgError(
                    MLG_E_HEADER,
                    f"header CRC32 mismatch: stored 0x{hdr.header_crc32:08X}, computed 0x{want:08X}",
                )
        return hdr


# --------------------------------------------------------------------------
# Event record
# --------------------------------------------------------------------------


@dataclass
class MlgEvent:
    kind: int = MLG_KIND_TEXT
    flags: int = 0
    sequence: int = 0
    conversation: int = 0
    prev_offset: int = 0
    timestamp: MlgTime = field(default_factory=MlgTime)
    chapter: int = 0
    zone_id: int = 0
    scene_id: int = 0xFFFF
    speaker_id: int = 0
    source_key: int = 0
    source_file: int = 0xFFFF
    fragment_index: int = 0
    speaker: bytes = b""
    location: bytes = b""
    body: bytes = b""
    # Populated on parse only:
    offset: int = 0
    record_length: int = 0
    event_crc32: int = 0

    def pack(self) -> bytes:
        if len(self.speaker) > MLG_MAX_SPEAKER:
            raise MlgError(MLG_E_RANGE, f"speaker {len(self.speaker)} > {MLG_MAX_SPEAKER}")
        if len(self.location) > MLG_MAX_LOCATION:
            raise MlgError(MLG_E_RANGE, f"location {len(self.location)} > {MLG_MAX_LOCATION}")
        if len(self.body) > MLG_MAX_BODY:
            raise MlgError(MLG_E_RANGE, f"body {len(self.body)} > {MLG_MAX_BODY}")
        total = MLG_EVENT_HEAD_SIZE + len(self.speaker) + len(self.location) + len(self.body) + 4
        buf = bytearray(MLG_EVENT_HEAD_SIZE)
        put_u32(buf, 0, total)
        put_u16(buf, 4, self.kind)
        put_u16(buf, 6, self.flags)
        put_u32(buf, 8, self.sequence)
        put_u32(buf, 12, self.conversation)
        put_u32(buf, 16, self.prev_offset)
        buf[20:28] = self.timestamp.pack()
        put_u16(buf, 28, self.chapter)
        put_u16(buf, 30, self.zone_id)
        put_u16(buf, 32, self.scene_id)
        put_u16(buf, 34, self.speaker_id)
        put_u32(buf, 36, self.source_key)
        put_u16(buf, 40, self.source_file)
        put_u16(buf, 42, self.fragment_index)
        put_u16(buf, 44, len(self.speaker))
        put_u16(buf, 46, len(self.location))
        put_u16(buf, 48, len(self.body))
        put_u16(buf, 50, 0)
        payload = bytes(buf) + self.speaker + self.location + self.body
        self.record_length = total
        self.event_crc32 = crc32(payload)
        tail = bytearray(4)
        put_u32(tail, 0, self.event_crc32)
        return payload + bytes(tail)

    @staticmethod
    def unpack(data: bytes, offset: int = 0, *, limit: int | None = None) -> MlgEvent:
        """Parse the record starting at ``offset`` inside ``data``.

        ``limit`` is the committed end of file; the record must fit entirely
        inside it.  Every length is bounds-checked before it is used as an
        index, exactly like the C core."""
        end_of_data = len(data) if limit is None else min(limit, len(data))
        if offset + 4 > end_of_data:
            raise MlgError(MLG_E_TRUNC, "record length field is past end of data", offset)
        total = get_u32(data, offset)
        if total < MLG_EVENT_MIN_RECORD or total > MLG_MAX_RECORD:
            raise MlgError(MLG_E_RANGE, f"illegal record_length {total}", offset)
        if offset + total > end_of_data:
            raise MlgError(MLG_E_TRUNC, f"record of {total} bytes runs past committed end", offset)
        if offset + MLG_EVENT_HEAD_SIZE > end_of_data:
            raise MlgError(MLG_E_TRUNC, "record head is truncated", offset)
        rec = data[offset : offset + total]
        stored_crc = get_u32(rec, total - 4)
        want = crc32(rec[: total - 4])
        if stored_crc != want:
            raise MlgError(
                MLG_E_CRC,
                f"event CRC32 mismatch: stored 0x{stored_crc:08X}, computed 0x{want:08X}",
                offset,
            )
        s_len = get_u16(rec, 44)
        l_len = get_u16(rec, 46)
        b_len = get_u16(rec, 48)
        if s_len > MLG_MAX_SPEAKER or l_len > MLG_MAX_LOCATION or b_len > MLG_MAX_BODY:
            raise MlgError(MLG_E_RANGE, "string length exceeds the per-field cap", offset)
        if MLG_EVENT_HEAD_SIZE + s_len + l_len + b_len + 4 != total:
            raise MlgError(MLG_E_RANGE, "string lengths do not add up to record_length", offset)
        p = MLG_EVENT_HEAD_SIZE
        speaker = bytes(rec[p : p + s_len])
        p += s_len
        location = bytes(rec[p : p + l_len])
        p += l_len
        body = bytes(rec[p : p + b_len])
        return MlgEvent(
            kind=get_u16(rec, 4),
            flags=get_u16(rec, 6),
            sequence=get_u32(rec, 8),
            conversation=get_u32(rec, 12),
            prev_offset=get_u32(rec, 16),
            timestamp=MlgTime.unpack(rec, 20),
            chapter=get_u16(rec, 28),
            zone_id=get_u16(rec, 30),
            scene_id=get_u16(rec, 32),
            speaker_id=get_u16(rec, 34),
            source_key=get_u32(rec, 36),
            source_file=get_u16(rec, 40),
            fragment_index=get_u16(rec, 42),
            speaker=speaker,
            location=location,
            body=body,
            offset=offset,
            record_length=total,
            event_crc32=stored_crc,
        )


# --------------------------------------------------------------------------
# Double-byte-safe fragment splitting
# --------------------------------------------------------------------------


def split_point(body: bytes, limit: int) -> int:
    """Longest prefix of ``body`` that is <= ``limit`` bytes and never cuts a
    BAK-ZH double-byte glyph in half.

    Trail bytes legitimately include 0x23 ('#') and 0x40 ('@'), so the scan must
    be lead-aware and run forward from the start of the fragment — never a
    backward search for an ASCII character."""
    if limit <= 0:
        return 0
    if len(body) <= limit:
        return len(body)
    i = 0
    last_safe = 0
    while i < len(body):
        b = body[i]
        step = 2 if (ZH_LEAD_MIN <= b <= ZH_LEAD_MAX and i + 1 < len(body)) else 1
        if i + step > limit:
            break
        i += step
        last_safe = i
    return last_safe


def split_body(body: bytes, limit: int = MLG_MAX_BODY) -> list[bytes]:
    """Split ``body`` into <=``limit``-byte, double-byte-safe fragments."""
    if limit <= 1:
        raise MlgError(MLG_E_PARAM, "fragment limit must be >= 2")
    out: list[bytes] = []
    rest = body
    while True:
        cut = split_point(rest, limit)
        if cut == 0:
            # A lone lead byte with no trail left: emit it verbatim rather than
            # spinning forever. The reader renders it as an unknown glyph.
            cut = min(len(rest), limit)
            if cut == 0:
                break
        out.append(rest[:cut])
        rest = rest[cut:]
        if not rest:
            break
    return out or [b""]


# --------------------------------------------------------------------------
# Whole-file model
# --------------------------------------------------------------------------


@dataclass
class MlgFile:
    header: MlgHeader = field(default_factory=MlgHeader)
    events: list[MlgEvent] = field(default_factory=list)
    # Bytes past header.committed_length that were present in the file. A
    # non-empty tail means the last append was interrupted.
    uncommitted_tail: int = 0

    # -- writing -----------------------------------------------------------
    def to_bytes(self, *, seal: bool = True, data_crc: bool = True) -> bytes:
        body = bytearray()
        prev = 0
        seq = self.header.next_sequence
        for ev in self.events:
            ev.prev_offset = prev
            if ev.sequence == 0:
                ev.sequence = seq
                seq += 1
            off = MLG_HEADER_SIZE + len(body)
            blob = ev.pack()
            ev.offset = off
            body += blob
            prev = off
        hdr = self.header
        hdr.committed_length = MLG_HEADER_SIZE + len(body)
        hdr.event_count = len(self.events)
        hdr.next_sequence = max([e.sequence for e in self.events], default=0) + 1
        hdr.last_event_offset = prev
        if data_crc:
            hdr.data_crc32 = crc32(bytes(body))
            hdr.flags |= MLG_HF_DATA_CRC
        else:
            hdr.data_crc32 = 0
            hdr.flags &= ~MLG_HF_DATA_CRC
        if seal:
            hdr.flags |= MLG_HF_SEALED
        else:
            hdr.flags &= ~MLG_HF_SEALED
        return hdr.pack() + bytes(body)

    def write(self, path: Path, **kw: Any) -> None:
        Path(path).write_bytes(self.to_bytes(**kw))

    # -- reading -----------------------------------------------------------
    @staticmethod
    def parse(
        data: bytes,
        *,
        expect_mapping: int | None = None,
        expect_gam: tuple[int, int] | None = None,
        strict_tail: bool = True,
    ) -> MlgFile:
        """Full validation pass, mirroring the DOS core's load-candidate path."""
        hdr = MlgHeader.unpack(data)
        if hdr.encoding_id != MLG_ENCODING_BAKZH_V1:
            raise MlgError(MLG_E_ENCODING, f"unknown encoding_id {hdr.encoding_id}")
        if expect_mapping is not None and hdr.mapping_fingerprint != expect_mapping:
            raise MlgError(
                MLG_E_ENCODING,
                f"mapping fingerprint mismatch: file 0x{hdr.mapping_fingerprint:08X}, "
                f"build 0x{expect_mapping:08X}",
            )
        if expect_gam is not None:
            if not hdr.flags & MLG_HF_GAM_BOUND:
                raise MlgError(MLG_E_BINDING, "snapshot carries no GAM binding")
            if (hdr.bound_gam_length, hdr.bound_gam_crc32) != expect_gam:
                raise MlgError(
                    MLG_E_BINDING,
                    f"GAM binding mismatch: file ({hdr.bound_gam_length}, "
                    f"0x{hdr.bound_gam_crc32:08X}) vs save "
                    f"({expect_gam[0]}, 0x{expect_gam[1]:08X})",
                )
        if hdr.committed_length < MLG_HEADER_SIZE:
            raise MlgError(MLG_E_RANGE, f"committed_length {hdr.committed_length} < header")
        if hdr.committed_length > MLG_MAX_FILE:
            raise MlgError(MLG_E_RANGE, "committed_length exceeds the format ceiling")
        if hdr.committed_length > len(data):
            raise MlgError(
                MLG_E_TRUNC,
                f"committed_length {hdr.committed_length} > file length {len(data)}",
            )
        if hdr.last_event_offset and not (
            MLG_HEADER_SIZE <= hdr.last_event_offset < hdr.committed_length
        ):
            raise MlgError(MLG_E_RANGE, f"last_event_offset 0x{hdr.last_event_offset:X} is outside")
        if hdr.flags & MLG_HF_DATA_CRC:
            want = crc32(data[MLG_HEADER_SIZE : hdr.committed_length])
            if want != hdr.data_crc32:
                raise MlgError(
                    MLG_E_CRC,
                    f"data CRC32 mismatch: stored 0x{hdr.data_crc32:08X}, computed 0x{want:08X}",
                )
        events: list[MlgEvent] = []
        off = MLG_HEADER_SIZE
        prev = 0
        while off < hdr.committed_length:
            ev = MlgEvent.unpack(data, off, limit=hdr.committed_length)
            if ev.prev_offset != prev:
                raise MlgError(
                    MLG_E_RANGE,
                    f"prev_offset 0x{ev.prev_offset:X} should be 0x{prev:X}",
                    off,
                )
            events.append(ev)
            prev = off
            off += ev.record_length
        if off != hdr.committed_length:
            raise MlgError(MLG_E_TRUNC, "last record does not land on committed_length", off)
        if strict_tail:
            if len(events) != hdr.event_count:
                raise MlgError(
                    MLG_E_RANGE,
                    f"event_count {hdr.event_count} but {len(events)} records present",
                )
            if hdr.last_event_offset != prev:
                raise MlgError(
                    MLG_E_RANGE,
                    f"last_event_offset 0x{hdr.last_event_offset:X} != 0x{prev:X}",
                )
        return MlgFile(header=hdr, events=events, uncommitted_tail=len(data) - hdr.committed_length)

    @staticmethod
    def read(path: Path, **kw: Any) -> MlgFile:
        return MlgFile.parse(Path(path).read_bytes(), **kw)


def recover_committed_length(data: bytes) -> tuple[int, int, int, int]:
    """Re-derive the committed tail by walking records forward from the header.

    This is the fallback the C core runs when the header CRC does not validate
    (or the header claims more than the file holds): it returns the longest
    verifiable prefix, never a guess.

    Returns ``(committed_length, event_count, next_sequence, last_event_offset)``."""
    off = MLG_HEADER_SIZE
    count = 0
    last = 0
    high_seq = 0
    while True:
        try:
            ev = MlgEvent.unpack(data, off)
        except MlgError:
            break
        count += 1
        last = off
        high_seq = max(high_seq, ev.sequence)
        off += ev.record_length
    return off, count, high_seq + 1, last


# --------------------------------------------------------------------------
# Encoding mapping fingerprint
# --------------------------------------------------------------------------

DEFAULT_MAPPING = Path("localization/generated/zh_mapping.json")


def mapping_fingerprint(mapping: dict[str, Any]) -> int:
    """CRC32 over a canonical serialization of the glyph mapping.

    Canonical stream (all little endian):
        u32 encoding_id (= 1)
        u32 entry_count
        then, sorted by glyph_id ascending: u32 glyph_id, u32 unicode_codepoint

    Deterministic, independent of JSON key order, and trivially reimplementable
    by a build step that emits the C constant."""
    char_to_id = mapping["char_to_id"]
    entries = sorted((int(gid), ord(ch)) for ch, gid in char_to_id.items())
    buf = bytearray(8)
    put_u32(buf, 0, MLG_ENCODING_BAKZH_V1)
    put_u32(buf, 4, len(entries))
    for gid, cp in entries:
        item = bytearray(8)
        put_u32(item, 0, gid)
        put_u32(item, 4, cp)
        buf += item
    return crc32(bytes(buf))


def load_mapping(path: Path | None = None) -> dict[str, Any]:
    p = Path(path) if path else DEFAULT_MAPPING
    return json.loads(p.read_text(encoding="utf-8"))


def decode_bytes(data: bytes, id_to_char: dict[int, str]) -> str:
    """BAK-ZH game bytes -> UTF-8 text, for diagnostics only."""
    from tools.font.build_font import decode_string

    return decode_string(data, id_to_char)


# --------------------------------------------------------------------------
# Hex fixture helpers (golden fixtures live as reviewable hex text, because the
# repo .gitignore excludes *.bin / *.gam-style binary blobs)
# --------------------------------------------------------------------------


def to_hex_text(data: bytes, width: int = 16) -> str:
    lines = []
    for i in range(0, len(data), width):
        chunk = data[i : i + width]
        lines.append(f"{i:08X}  " + " ".join(f"{b:02X}" for b in chunk))
    return "\n".join(lines) + "\n"


def from_hex_text(text: str) -> bytes:
    out = bytearray()
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        parts = line.split()
        if parts and parts[0].endswith(":"):
            parts = parts[1:]
        elif len(parts) > 1 and len(parts[0]) == 8:
            parts = parts[1:]
        for tok in parts:
            out.append(int(tok, 16))
    return bytes(out)


# --------------------------------------------------------------------------
# The canonical cross-language fixture
#
# `MLGTEST GEN` (bak/TOOLS/MLGTEST/MLGTEST.C, built by the period Borland
# toolchain and linking the game's own MSGLOG.C) writes exactly these bytes.
# Keeping the script in one place is what makes the C->Python direction a real
# assertion rather than "both sides agree with themselves".
# --------------------------------------------------------------------------

# The MSGLOG_MAPPING_FINGERPRINT constant pinned in bak/SRC/DIALOG/MSGLOG.H.
# tests/unit/test_message_log.py asserts it still equals mapping_fingerprint()
# of localization/generated/zh_mapping.json.
MSGLOG_MAPPING_FINGERPRINT = 0x9659C961


SCRIPTED_CREATED = MlgTime(2026, 9, 6, 13, 45, 7, 25)

# "納馮" / "三山當鋪" in BAK-ZH.
SCRIPTED_SPEAKER = bytes([0x84, 0x32, 0x96, 0x49])
SCRIPTED_LOCATION = bytes([0x85, 0x43, 0x80, 0x24, 0x81, 0x34, 0x99, 0x3D])
# '"Hello!" ' + 漫(80 23) + 抵(80 40) + 數(81 23) + '#end@'.
# Two of those glyphs carry a trail byte that is literally '#' (0x23) and '@'
# (0x40) — the two characters the dialog layer treats as title delimiter and
# token marker. They must survive byte-exact.
SCRIPTED_BODY = bytes(
    [0x22, 0x48, 0x65, 0x6C, 0x6C, 0x6F, 0x21, 0x22, 0x20]
    + [0x80, 0x23, 0x80, 0x40, 0x81, 0x23]
    + [0x23, 0x65, 0x6E, 0x64, 0x40]
)
SCRIPTED_CHOICE = bytes([0x80, 0x40, 0x82, 0x23])
# 'A' + 300 double-byte glyphs = 601 bytes. A naive 512-byte cut would fall
# between the lead and trail of the glyph occupying bytes 511/512.
SCRIPTED_LONG = b"A" + bytes([0x80, 0x23]) * 300

_SCRIPTED_CTX = dict(
    chapter=1,
    zone_id=9,
    scene_id=7,
    speaker_id=7,
    source_key=1600006,
    source_file=16,
    speaker=SCRIPTED_SPEAKER,
    location=SCRIPTED_LOCATION,
)
_EMPTY_CTX = dict(
    chapter=0, zone_id=0, scene_id=0xFFFF, speaker_id=0, source_key=0, source_file=0xFFFF
)


def build_scripted_fixture() -> bytes:
    """Byte-for-byte what `MLGTEST GEN` produces, built independently here."""
    frag0 = SCRIPTED_LONG[:511]
    frag1 = SCRIPTED_LONG[511:]
    assert len(frag0) == 511 and len(frag1) == 90
    events = [
        MlgEvent(
            kind=MLG_KIND_CONV_BEGIN,
            sequence=1,
            conversation=1,
            timestamp=MlgTime(2026, 9, 6, 13, 45, 8, 0),
            **_SCRIPTED_CTX,
        ),
        MlgEvent(
            kind=MLG_KIND_TEXT,
            sequence=2,
            conversation=1,
            timestamp=MlgTime(2026, 9, 6, 13, 45, 9, 10),
            body=SCRIPTED_BODY,
            **_SCRIPTED_CTX,
        ),
        MlgEvent(
            kind=MLG_KIND_CHOICE,
            sequence=3,
            conversation=1,
            timestamp=MlgTime(2026, 9, 6, 13, 45, 10, 20),
            body=SCRIPTED_CHOICE,
            **_SCRIPTED_CTX,
        ),
        MlgEvent(
            kind=MLG_KIND_TEXT,
            sequence=4,
            conversation=1,
            flags=MLG_EV_MORE,
            fragment_index=0,
            timestamp=MlgTime(2026, 9, 6, 13, 45, 11, 30),
            body=frag0,
            **_SCRIPTED_CTX,
        ),
        MlgEvent(
            kind=MLG_KIND_TEXT,
            sequence=5,
            conversation=1,
            flags=MLG_EV_CONTINUED,
            fragment_index=1,
            timestamp=MlgTime(2026, 9, 6, 13, 45, 11, 30),
            body=frag1,
            **_SCRIPTED_CTX,
        ),
        MlgEvent(
            kind=MLG_KIND_GAP,
            sequence=6,
            conversation=1,
            timestamp=MlgTime(2026, 9, 6, 13, 45, 12, 40),
            **_EMPTY_CTX,
        ),
        MlgEvent(
            kind=MLG_KIND_CONV_END,
            sequence=7,
            conversation=1,
            timestamp=MlgTime(2026, 9, 6, 13, 45, 13, 50),
            **_EMPTY_CTX,
        ),
    ]
    hdr = MlgHeader(
        flags=MLG_HF_HAS_GAP | MLG_HF_SEALED,
        mapping_fingerprint=MSGLOG_MAPPING_FINGERPRINT,
        created_time=SCRIPTED_CREATED,
    )
    return MlgFile(header=hdr, events=events).to_bytes(seal=True, data_crc=False)


def build_python_fixture() -> bytes:
    """A small, deliberately different timeline written by Python for the DOS
    core to read back — the other half of the cross-language check."""
    ctx = dict(
        chapter=3,
        zone_id=12,
        scene_id=0xFFFF,
        speaker_id=33,
        source_key=1300001,
        source_file=13,
        speaker=SCRIPTED_LOCATION,
        location=SCRIPTED_SPEAKER,
    )
    events = [
        MlgEvent(
            kind=MLG_KIND_SCENE,
            sequence=1,
            conversation=0,
            timestamp=MlgTime(2026, 9, 6, 14, 0, 1, 5),
            body=SCRIPTED_CHOICE + b"@#",
            **ctx,
        ),
        MlgEvent(
            kind=MLG_KIND_TEXT,
            sequence=2,
            conversation=0,
            flags=MLG_EV_NARRATION,
            timestamp=MlgTime(2026, 9, 6, 14, 0, 2, 15),
            body=SCRIPTED_BODY,
            **{**ctx, "speaker": b"", "speaker_id": 0},
        ),
    ]
    hdr = MlgHeader(
        flags=0,
        mapping_fingerprint=MSGLOG_MAPPING_FINGERPRINT,
        created_time=MlgTime(2026, 9, 6, 14, 0, 0, 0),
    )
    return MlgFile(header=hdr, events=events).to_bytes(seal=True, data_crc=False)


def build_snapshot_fixture(gam_length: int, gam_crc: int, *, events: int = 3) -> bytes:
    """A sealed snapshot bound to a (length, CRC32) game-file fingerprint."""
    ctx = dict(
        chapter=2, zone_id=4, scene_id=0xFFFF, speaker_id=50, source_key=71, source_file=0
    )
    evs = [
        MlgEvent(
            kind=MLG_KIND_TEXT,
            sequence=i + 1,
            conversation=0,
            timestamp=MlgTime(2026, 9, 6, 15, 0, i, 0),
            body=b"snapshot event %d" % i,
            **ctx,
        )
        for i in range(events)
    ]
    hdr = MlgHeader(
        flags=MLG_HF_SNAPSHOT | MLG_HF_SEALED | MLG_HF_GAM_BOUND,
        mapping_fingerprint=MSGLOG_MAPPING_FINGERPRINT,
        bound_gam_length=gam_length,
        bound_gam_crc32=gam_crc,
        created_time=MlgTime(2026, 9, 6, 15, 0, 0, 0),
    )
    return MlgFile(header=hdr, events=evs).to_bytes(seal=True, data_crc=True)


def build_large_fixture(target_bytes: int = 80 * 1024) -> bytes:
    """A timeline whose total length crosses 64 KiB, so every offset the DOS
    core computes has to be a real 32-bit value, not a 16-bit one."""
    ctx = dict(
        chapter=1, zone_id=1, scene_id=0xFFFF, speaker_id=7, source_key=1, source_file=0
    )
    body = bytes([0x80, 0x23]) * 200  # 400 bytes
    evs: list[MlgEvent] = []
    size = MLG_HEADER_SIZE
    i = 0
    while size < target_bytes:
        evs.append(
            MlgEvent(
                kind=MLG_KIND_TEXT,
                sequence=i + 1,
                conversation=0,
                timestamp=MlgTime(2026, 9, 6, 16, 0, i % 60, 0),
                body=body,
                **ctx,
            )
        )
        size += MLG_EVENT_HEAD_SIZE + len(body) + 4
        i += 1
    hdr = MlgHeader(
        flags=0,
        mapping_fingerprint=MSGLOG_MAPPING_FINGERPRINT,
        created_time=MlgTime(2026, 9, 6, 16, 0, 0, 0),
    )
    return MlgFile(header=hdr, events=evs).to_bytes(seal=True, data_crc=False)


def _bad_len_bytes(good: bytes) -> bytearray:
    """Corrupt the 3rd record's length field to an impossible value."""
    off3 = MLG_HEADER_SIZE + 68 + 88
    bad = bytearray(good)
    bad[off3 : off3 + 4] = b"\xff\xff\x00\x00"
    return bad


def build_corrupt_snapshot_fixture() -> bytes:
    """A *snapshot* carrying the same mid-file length corruption, with
    ``data_crc32`` recomputed so the damage survives the whole-history checksum.

    Only the structural pass in ``msglog_load_candidate()`` can reject this, so
    it proves that pass is real and not shadowed by the CRC check."""
    bad = _bad_len_bytes(build_scripted_fixture())
    hdr = MlgHeader.unpack(bytes(bad))
    hdr.flags |= MLG_HF_SNAPSHOT | MLG_HF_DATA_CRC | MLG_HF_GAM_BOUND
    hdr.bound_gam_length = 1
    hdr.bound_gam_crc32 = 2
    hdr.data_crc32 = crc32(bytes(bad[MLG_HEADER_SIZE : hdr.committed_length]))
    return hdr.pack() + bytes(bad[MLG_HEADER_SIZE:])


def _corrupt(data: bytes, offset: int, value: int) -> bytes:
    out = bytearray(data)
    out[offset] = value
    return bytes(out)


def build_invalid_fixtures() -> dict[str, tuple[bytes, str]]:
    """Damaged files, each paired with the behaviour the DOS core must show.

    The second element names the expected outcome of `msglog_open_working()`:
    either ``reject:<code>`` (a distinguishable refusal) or ``prefix:<n>``
    (accepted, with exactly *n* events recovered from the verifiable prefix)."""
    good = build_scripted_fixture()
    out: dict[str, tuple[bytes, str]] = {}

    out["EMPTY"] = (b"", f"reject:{MLG_E_TRUNC}")
    out["SHORTHDR"] = (good[:32], f"reject:{MLG_E_TRUNC}")
    out["BADMAGIC"] = (b"XXXX" + good[4:], f"reject:{MLG_E_MAGIC}")

    h = MlgHeader.unpack(good)
    h.format_version = 2
    out["BADVER"] = (h.pack() + good[MLG_HEADER_SIZE:], f"reject:{MLG_E_VERSION}")

    h = MlgHeader.unpack(good)
    h.format_version = MLG_FORMAT_VERSION
    h.mapping_fingerprint = 0xDEADBEEF
    out["BADFP"] = (h.pack() + good[MLG_HEADER_SIZE:], f"reject:{MLG_E_ENCODING}")

    # Header CRC destroyed -> the core must fall back to the forward rescan and
    # still recover all seven events.
    out["BADHCRC"] = (_corrupt(good, 60, good[60] ^ 0xFF), "prefix:7")

    # Last record's CRC destroyed -> six events survive.
    out["BADECRC"] = (_corrupt(good, len(good) - 1, good[-1] ^ 0xFF), "prefix:6")

    # File cut inside the last record; the header still claims the full length.
    out["TRUNCEV"] = (good[: len(good) - 20], "prefix:6")

    # Illegal record_length in the middle of the stream. The header is untouched
    # and still validates, and so does the *last* record — so msglog_open_working()
    # deliberately trusts the header and reports all seven. That is the documented
    # cheap-open policy: a working file is re-scanned only when its header or its
    # tail record fails. Mid-file damage is caught by the reader (every
    # msglog_next_offset / msglog_read_event verifies the record it touches) and,
    # for a save-slot file, by the full structural pass in msglog_load_candidate()
    # — see build_corrupt_snapshot_fixture().
    out["BADLEN"] = (bytes(_bad_len_bytes(good)), "prefix:7")

    # last_event_offset points past committed_length -> header rejected, rescan.
    h = MlgHeader.unpack(good)
    h.last_event_offset = h.committed_length + 4096
    out["BIGOFF"] = (h.pack() + good[MLG_HEADER_SIZE:], "prefix:7")

    # body_len 513 exceeds MSGLOG_MAX_BODY. The record is otherwise complete and
    # self-consistent, so the only thing that can stop it is the explicit cap
    # check the reader runs *before* it uses the length as a size.
    over = MLG_MAX_BODY + 1
    head = bytearray(MLG_EVENT_HEAD_SIZE)
    put_u32(head, 0, MLG_EVENT_HEAD_SIZE + over + 4)
    put_u16(head, 4, MLG_KIND_TEXT)
    put_u32(head, 8, 1)
    head[20:28] = MlgTime(2026, 9, 6, 17, 0, 0, 0).pack()
    put_u16(head, 32, 0xFFFF)
    put_u16(head, 40, 0xFFFF)
    put_u16(head, 48, over)
    blob = bytearray(bytes(head) + b"\x41" * over + b"\x00\x00\x00\x00")
    put_u32(blob, len(blob) - 4, crc32(bytes(blob[: len(blob) - 4])))
    hdr = MlgHeader(
        flags=MLG_HF_SEALED,
        mapping_fingerprint=MSGLOG_MAPPING_FINGERPRINT,
        committed_length=MLG_HEADER_SIZE + len(blob),
        event_count=1,
        next_sequence=2,
        last_event_offset=MLG_HEADER_SIZE,
        created_time=SCRIPTED_CREATED,
    )
    out["TOOBIG"] = (hdr.pack() + bytes(blob), "prefix:0")

    return out


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------


def _dump(path: Path, mapping_path: Path | None, out: Any) -> int:
    data = Path(path).read_bytes()
    try:
        mlg = MlgFile.parse(data, strict_tail=False)
    except MlgError as exc:
        print(f"INVALID: {exc}", file=out)
        rec = recover_committed_length(data)
        print(f"verifiable prefix: committed_length={rec[0]} events={rec[1]}", file=out)
        return 1
    id_to_char: dict[int, str] = {}
    try:
        mapping = load_mapping(mapping_path)
        id_to_char = {int(v): k for k, v in mapping["char_to_id"].items()}
    except (OSError, KeyError, ValueError):
        print("(no mapping available — bodies shown as raw hex)", file=out)
    h = mlg.header
    print(f"file          : {path}", file=out)
    print(f"format version: {h.format_version}", file=out)
    print(f"flags         : 0x{h.flags:04X}", file=out)
    print(f"encoding      : {h.encoding_id}  mapping fp 0x{h.mapping_fingerprint:08X}", file=out)
    print(f"bound GAM     : len={h.bound_gam_length} crc=0x{h.bound_gam_crc32:08X}", file=out)
    print(f"committed     : {h.committed_length} bytes, {h.event_count} events", file=out)
    print(f"next sequence : {h.next_sequence}", file=out)
    print(f"created       : {h.created_time}", file=out)
    print(f"uncommitted   : {mlg.uncommitted_tail} trailing bytes", file=out)
    print("", file=out)
    for ev in mlg.events:
        name = KIND_NAMES.get(ev.kind, f"UNKNOWN(0x{ev.kind:04X})")
        who = decode_bytes(ev.speaker, id_to_char) if id_to_char else ev.speaker.hex()
        where = decode_bytes(ev.location, id_to_char) if id_to_char else ev.location.hex()
        what = decode_bytes(ev.body, id_to_char) if id_to_char else ev.body.hex()
        print(
            f"[{ev.sequence:5d}] @0x{ev.offset:06X} {name:<10} conv={ev.conversation} "
            f"key={ev.source_key} spk={ev.speaker_id} frag={ev.fragment_index} "
            f"flags=0x{ev.flags:04X}",
            file=out,
        )
        print(f"         when : {ev.timestamp}", file=out)
        print(f"         who  : {who or '(narration)'}", file=out)
        print(f"         where: {where or '(unknown)'}", file=out)
        print(f"         what : {what}", file=out)
    return 0


def main(argv: list[str] | None = None) -> int:
    import sys

    ap = argparse.ArgumentParser(description="MLG v1 message-log codec / validator")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("dump", help="print a UTF-8 diagnostic listing")
    p.add_argument("file", type=Path)
    p.add_argument("--mapping", type=Path, default=None)

    p = sub.add_parser("verify", help="validate; exit 0 only if fully valid")
    p.add_argument("file", type=Path)
    p.add_argument("--mapping-fingerprint", type=lambda s: int(s, 0), default=None)

    p = sub.add_parser("fingerprint", help="print the encoding mapping fingerprint")
    p.add_argument("--mapping", type=Path, default=None)
    p.add_argument("--c-define", action="store_true", help="emit the C header constant")

    p = sub.add_parser("hex2bin", help="hex fixture -> binary")
    p.add_argument("src", type=Path)
    p.add_argument("dst", type=Path)

    p = sub.add_parser("bin2hex", help="binary -> hex fixture")
    p.add_argument("src", type=Path)
    p.add_argument("dst", type=Path)

    args = ap.parse_args(argv)

    if args.cmd == "dump":
        return _dump(args.file, args.mapping, sys.stdout)
    if args.cmd == "verify":
        try:
            mlg = MlgFile.read(args.file, expect_mapping=args.mapping_fingerprint)
        except MlgError as exc:
            print(f"FAIL {exc}")
            return 1
        print(f"OK {mlg.header.event_count} events, {mlg.header.committed_length} bytes committed")
        return 0
    if args.cmd == "fingerprint":
        fp = mapping_fingerprint(load_mapping(args.mapping))
        if args.c_define:
            print(f"#define MSGLOG_MAPPING_FINGERPRINT 0x{fp:08X}UL")
        else:
            print(f"0x{fp:08X}")
        return 0
    if args.cmd == "hex2bin":
        args.dst.write_bytes(from_hex_text(args.src.read_text(encoding="utf-8")))
        return 0
    if args.cmd == "bin2hex":
        args.dst.write_text(to_hex_text(args.src.read_bytes()), encoding="utf-8")
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
