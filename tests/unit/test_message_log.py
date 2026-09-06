"""
Unit tests for the MLG v1 message-log container (docs/research/message-log-format.md).

These assert the *file contract* — byte offsets, checksum ranges, bounds
checking, recovery behaviour — against golden fixtures on disk, not against the
C source. The matching DOS-side conformance run (bak/TOOLS/MLGTEST) is driven by
tools/text/mlg_dos_check.py and covers the cross-language direction.
"""

import json
import re
import unittest
from pathlib import Path

from tools.font.build_font import decode_string
from tools.text.message_log import (
    MLG_E_CRC,
    MLG_E_ENCODING,
    MLG_E_MAGIC,
    MLG_E_RANGE,
    MLG_E_TRUNC,
    MLG_E_VERSION,
    MLG_EVENT_HEAD_SIZE,
    MLG_EV_CONTINUED,
    MLG_EV_MORE,
    MLG_FORMAT_VERSION,
    MLG_HEADER_SIZE,
    MLG_HF_DATA_CRC,
    MLG_HF_GAM_BOUND,
    MLG_HF_HAS_GAP,
    MLG_HF_SEALED,
    MLG_HF_SNAPSHOT,
    MLG_KIND_CHOICE,
    MLG_KIND_CONV_BEGIN,
    MLG_KIND_CONV_END,
    MLG_KIND_GAP,
    MLG_KIND_TEXT,
    MLG_MAGIC,
    MLG_MAX_BODY,
    MLG_MAX_RECORD,
    MSGLOG_MAPPING_FINGERPRINT,
    SCRIPTED_BODY,
    SCRIPTED_CREATED,
    SCRIPTED_LOCATION,
    SCRIPTED_LONG,
    SCRIPTED_SPEAKER,
    MlgError,
    MlgEvent,
    MlgFile,
    MlgHeader,
    MlgTime,
    build_invalid_fixtures,
    build_large_fixture,
    build_python_fixture,
    build_corrupt_snapshot_fixture,
    build_scripted_fixture,
    build_snapshot_fixture,
    crc32,
    from_hex_text,
    get_u16,
    get_u32,
    load_mapping,
    mapping_fingerprint,
    put_u32,
    recover_committed_length,
    split_body,
    split_point,
    to_hex_text,
)

REPO = Path(__file__).resolve().parents[2]
FIXTURES = REPO / "tests" / "fixtures" / "message_log"
MSGLOG_H = REPO / "upstream" / "betrayal-at-krondor" / "bak" / "SRC" / "DIALOG" / "MSGLOG.H"


def read_fixture(name: str) -> bytes:
    return from_hex_text((FIXTURES / f"{name}.mlg.hex").read_text(encoding="utf-8"))


class TestGoldenFixtures(unittest.TestCase):
    """The two hand-checkable fixtures, field by field."""

    def test_empty_timeline_is_64_bytes_and_hand_checkable(self):
        data = read_fixture("fixture_empty")
        self.assertEqual(len(data), MLG_HEADER_SIZE)
        self.assertEqual(data[0:4], MLG_MAGIC)
        self.assertEqual(get_u16(data, 4), MLG_FORMAT_VERSION)
        self.assertEqual(get_u16(data, 6), MLG_HEADER_SIZE)
        self.assertEqual(get_u16(data, 8), MLG_HF_SEALED)
        self.assertEqual(get_u16(data, 10), 1)
        self.assertEqual(get_u32(data, 12), MSGLOG_MAPPING_FINGERPRINT)
        self.assertEqual(get_u32(data, 24), MLG_HEADER_SIZE)  # committed_length
        self.assertEqual(get_u32(data, 28), 0)  # event_count
        self.assertEqual(get_u32(data, 32), 1)  # next_sequence
        self.assertEqual(get_u32(data, 36), 0)  # last_event_offset
        self.assertEqual(get_u32(data, 40), 0)  # data_crc32 (not computed)
        self.assertEqual(MlgTime.unpack(data, 44), SCRIPTED_CREATED)
        # The header checksum covers exactly bytes 0..59.
        self.assertEqual(get_u32(data, 60), crc32(data[:60]))

        mlg = MlgFile.parse(data)
        self.assertEqual(mlg.events, [])
        self.assertEqual(mlg.uncommitted_tail, 0)

    def test_single_event_fixture_offsets(self):
        data = read_fixture("fixture_one_event")
        self.assertEqual(len(data), MLG_HEADER_SIZE + 73)
        rec = data[MLG_HEADER_SIZE:]
        self.assertEqual(get_u32(rec, 0), 73)  # 52 head + 4 + 7 + 6 + 4 crc
        self.assertEqual(get_u16(rec, 4), MLG_KIND_TEXT)
        self.assertEqual(get_u32(rec, 8), 1)  # sequence
        self.assertEqual(get_u32(rec, 12), 1)  # conversation
        self.assertEqual(get_u32(rec, 16), 0)  # prev_offset: first record
        self.assertEqual(get_u16(rec, 34), 7)  # speaker_id
        self.assertEqual(get_u32(rec, 36), 1600006)  # source_key
        self.assertEqual((get_u16(rec, 44), get_u16(rec, 46), get_u16(rec, 48)), (4, 7, 6))
        p = MLG_EVENT_HEAD_SIZE
        self.assertEqual(rec[p : p + 4], b"Owyn")
        self.assertEqual(rec[p + 4 : p + 11], b"Krondor")
        self.assertEqual(rec[p + 11 : p + 17], b"Hello.")
        # The event checksum covers the record minus its own trailing 4 bytes.
        self.assertEqual(get_u32(rec, 69), crc32(rec[:69]))

    def test_fixtures_match_the_builders(self):
        self.assertEqual(read_fixture("fixture_scripted"), build_scripted_fixture())
        self.assertEqual(read_fixture("fixture_python"), build_python_fixture())

    def test_hex_round_trip(self):
        blob = build_scripted_fixture()
        self.assertEqual(from_hex_text(to_hex_text(blob)), blob)


class TestScriptedTimeline(unittest.TestCase):
    """The multi-event fixture the DOS harness also produces."""

    def setUp(self):
        self.mlg = MlgFile.parse(build_scripted_fixture())

    def test_event_sequence_and_kinds(self):
        kinds = [e.kind for e in self.mlg.events]
        self.assertEqual(
            kinds,
            [
                MLG_KIND_CONV_BEGIN,
                MLG_KIND_TEXT,
                MLG_KIND_CHOICE,
                MLG_KIND_TEXT,
                MLG_KIND_TEXT,
                MLG_KIND_GAP,
                MLG_KIND_CONV_END,
            ],
        )
        self.assertEqual([e.sequence for e in self.mlg.events], [1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(self.mlg.header.next_sequence, 8)
        self.assertEqual(self.mlg.header.event_count, 7)

    def test_conversation_id_is_the_begin_records_sequence(self):
        self.assertTrue(all(e.conversation == 1 for e in self.mlg.events))

    def test_prev_offset_chain_walks_backwards(self):
        offsets = [e.offset for e in self.mlg.events]
        back = []
        cur = self.mlg.events[-1]
        while True:
            back.append(cur.offset)
            if cur.prev_offset == 0:
                break
            cur = next(e for e in self.mlg.events if e.offset == cur.prev_offset)
        self.assertEqual(list(reversed(back)), offsets)
        self.assertEqual(self.mlg.header.last_event_offset, offsets[-1])

    def test_gap_sets_the_header_flag(self):
        self.assertTrue(self.mlg.header.flags & MLG_HF_HAS_GAP)
        self.assertTrue(self.mlg.header.flags & MLG_HF_SEALED)
        self.assertFalse(self.mlg.header.flags & MLG_HF_SNAPSHOT)
        self.assertFalse(self.mlg.header.flags & MLG_HF_DATA_CRC)

    def test_snapshot_speaker_and_location_are_stored_verbatim(self):
        ev = self.mlg.events[1]
        self.assertEqual(ev.speaker, SCRIPTED_SPEAKER)
        self.assertEqual(ev.location, SCRIPTED_LOCATION)

    def test_chinese_trail_bytes_hash_and_at_survive(self):
        """A BAK-ZH trail byte may be '#' (0x23) or '@' (0x40) — the dialog
        layer's title delimiter and token marker. Storage must be byte-exact."""
        body = self.mlg.events[1].body
        self.assertEqual(body, SCRIPTED_BODY)
        self.assertIn(bytes([0x80, 0x23]), body)  # trail == '#'
        self.assertIn(bytes([0x80, 0x40]), body)  # trail == '@'
        mapping = load_mapping()
        id_to_char = {int(v): k for k, v in mapping["char_to_id"].items()}
        text = decode_string(body, id_to_char)
        self.assertIn("漫", text)
        self.assertIn("抵", text)
        self.assertIn("數", text)
        self.assertTrue(text.startswith('"Hello!" '))
        self.assertTrue(text.endswith("#end@"))

    def test_long_body_splits_without_cutting_a_glyph(self):
        a, b = self.mlg.events[3], self.mlg.events[4]
        self.assertEqual(len(a.body), 511, "a naive 512-byte cut would split a glyph")
        self.assertEqual(len(b.body), 90)
        self.assertEqual(a.flags & MLG_EV_MORE, MLG_EV_MORE)
        self.assertEqual(a.flags & MLG_EV_CONTINUED, 0)
        self.assertEqual(b.flags & MLG_EV_CONTINUED, MLG_EV_CONTINUED)
        self.assertEqual(b.flags & MLG_EV_MORE, 0)
        self.assertEqual((a.fragment_index, b.fragment_index), (0, 1))
        self.assertEqual(a.body + b.body, SCRIPTED_LONG)
        self.assertNotEqual(a.body[-1], 0x80, "fragment must not end on a lead byte")

    def test_every_record_is_within_the_size_cap(self):
        for e in self.mlg.events:
            self.assertLessEqual(e.record_length, MLG_MAX_RECORD)
            self.assertLessEqual(len(e.body), MLG_MAX_BODY)


class TestSplitting(unittest.TestCase):
    def test_split_point_never_lands_between_lead_and_trail(self):
        data = bytes([0x41, 0x42, 0x80, 0x23, 0x80, 0x40, 0x43, 0x44])
        # limit 0..8 -> the longest safe prefix
        self.assertEqual([split_point(data, n) for n in range(9)], [0, 1, 2, 2, 4, 4, 6, 7, 8])

    def test_split_point_returns_zero_for_a_lone_lead(self):
        self.assertEqual(split_point(bytes([0x80, 0x23, 0x41]), 1), 0)

    def test_split_body_reassembles_exactly(self):
        parts = split_body(SCRIPTED_LONG, MLG_MAX_BODY)
        self.assertEqual(b"".join(parts), SCRIPTED_LONG)
        self.assertEqual([len(p) for p in parts], [511, 90])

    def test_split_body_of_pure_ascii(self):
        parts = split_body(b"x" * 1100, MLG_MAX_BODY)
        self.assertEqual([len(p) for p in parts], [512, 512, 76])


class TestRejections(unittest.TestCase):
    """Each malformed input must fail for a distinguishable, documented reason."""

    def _code(self, data: bytes, **kw) -> int:
        with self.assertRaises(MlgError) as cm:
            MlgFile.parse(data, **kw)
        return cm.exception.code

    def test_empty_file(self):
        self.assertEqual(self._code(b""), MLG_E_TRUNC)

    def test_truncated_header(self):
        self.assertEqual(self._code(build_scripted_fixture()[:32]), MLG_E_TRUNC)

    def test_bad_magic(self):
        self.assertEqual(self._code(b"XXXX" + build_scripted_fixture()[4:]), MLG_E_MAGIC)

    def test_unknown_format_version(self):
        h = MlgHeader.unpack(build_scripted_fixture())
        h.format_version = 2
        blob = h.pack() + build_scripted_fixture()[MLG_HEADER_SIZE:]
        self.assertEqual(self._code(blob), MLG_E_VERSION)

    def test_mapping_fingerprint_mismatch(self):
        blob = build_scripted_fixture()
        self.assertEqual(
            self._code(blob, expect_mapping=MSGLOG_MAPPING_FINGERPRINT ^ 1), MLG_E_ENCODING
        )
        # And the same file passes when the fingerprint does match.
        MlgFile.parse(blob, expect_mapping=MSGLOG_MAPPING_FINGERPRINT)

    def test_truncated_event(self):
        self.assertEqual(self._code(build_scripted_fixture()[:-20]), MLG_E_TRUNC)

    def test_bad_event_crc(self):
        blob = bytearray(build_scripted_fixture())
        blob[-1] ^= 0xFF
        self.assertEqual(self._code(bytes(blob)), MLG_E_CRC)

    def test_bad_header_crc(self):
        blob = bytearray(build_scripted_fixture())
        blob[60] ^= 0xFF
        with self.assertRaises(MlgError) as cm:
            MlgFile.parse(bytes(blob))
        self.assertEqual(cm.exception.code, -8)  # MLG_E_HEADER

    def test_illegal_record_length(self):
        blob = bytearray(build_scripted_fixture())
        off = MLG_HEADER_SIZE
        put_u32(blob, off, 0xFFFF)
        self.assertEqual(self._code(bytes(blob)), MLG_E_RANGE)

    def test_record_length_below_the_minimum(self):
        blob = bytearray(build_scripted_fixture())
        put_u32(blob, MLG_HEADER_SIZE, 8)
        self.assertEqual(self._code(bytes(blob)), MLG_E_RANGE)

    def test_last_event_offset_out_of_range(self):
        h = MlgHeader.unpack(build_scripted_fixture())
        h.last_event_offset = h.committed_length + 4096
        blob = h.pack() + build_scripted_fixture()[MLG_HEADER_SIZE:]
        self.assertEqual(self._code(blob), MLG_E_RANGE)

    def test_committed_length_past_end_of_file(self):
        h = MlgHeader.unpack(build_scripted_fixture())
        h.committed_length += 512
        blob = h.pack() + build_scripted_fixture()[MLG_HEADER_SIZE:]
        self.assertEqual(self._code(blob), MLG_E_TRUNC)

    def test_mid_file_length_damage_in_a_snapshot_is_caught_structurally(self):
        """data_crc32 is recomputed over the damaged bytes, so only the
        per-record structural pass can reject this file."""
        blob = build_corrupt_snapshot_fixture()
        # The whole-history CRC agrees with the damaged bytes...
        h = MlgHeader.unpack(blob)
        self.assertEqual(h.data_crc32, crc32(blob[MLG_HEADER_SIZE : h.committed_length]))
        # ...and it is still refused, for the right reason.
        self.assertEqual(self._code(blob, expect_gam=(1, 2)), MLG_E_RANGE)

    def test_body_length_over_the_fragment_cap(self):
        data, expectation = build_invalid_fixtures()["TOOBIG"]
        self.assertEqual(expectation, "prefix:0")
        self.assertEqual(self._code(data), MLG_E_RANGE)

    def test_string_lengths_must_add_up_to_record_length(self):
        blob = bytearray(build_scripted_fixture())
        off = MLG_HEADER_SIZE + 68  # the 20-byte TEXT record
        blob[off + 48] = 19  # body_len one short
        put_u32(blob, off + get_u32(bytes(blob), off) - 4, crc32(bytes(blob[off : off + 84])))
        self.assertEqual(self._code(bytes(blob)), MLG_E_RANGE)

    def test_snapshot_binding_mismatch(self):
        blob = build_snapshot_fixture(12345, 0xAABBCCDD)
        MlgFile.parse(blob, expect_gam=(12345, 0xAABBCCDD))
        with self.assertRaises(MlgError) as cm:
            MlgFile.parse(blob, expect_gam=(12345, 0x11223344))
        self.assertEqual(cm.exception.code, -13)  # MLG_E_BINDING

    def test_snapshot_data_crc_mismatch(self):
        blob = bytearray(build_snapshot_fixture(1, 2))
        self.assertTrue(MlgHeader.unpack(bytes(blob)).flags & MLG_HF_DATA_CRC)
        self.assertTrue(MlgHeader.unpack(bytes(blob)).flags & MLG_HF_GAM_BOUND)
        h = MlgHeader.unpack(bytes(blob))
        h.data_crc32 ^= 0xFFFF
        blob = bytearray(h.pack() + bytes(blob)[MLG_HEADER_SIZE:])
        self.assertEqual(self._code(bytes(blob)), MLG_E_CRC)


class TestRecovery(unittest.TestCase):
    """An interrupted append must cost only the partial record."""

    def test_verifiable_prefix_after_a_corrupt_last_record(self):
        blob = bytearray(build_scripted_fixture())
        blob[-1] ^= 0xFF
        committed, count, next_seq, last = recover_committed_length(bytes(blob))
        self.assertEqual(count, 6)
        self.assertEqual(next_seq, 7)
        good = MlgFile.parse(build_scripted_fixture())
        self.assertEqual(committed, good.events[-1].offset)
        self.assertEqual(last, good.events[-2].offset)

    def test_verifiable_prefix_after_truncation(self):
        blob = build_scripted_fixture()[:-20]
        committed, count, _, _ = recover_committed_length(blob)
        self.assertEqual(count, 6)
        self.assertLess(committed, len(blob))

    def test_rescan_recovers_everything_when_only_the_header_is_damaged(self):
        blob = bytearray(build_scripted_fixture())
        blob[60] ^= 0xFF
        committed, count, next_seq, last = recover_committed_length(bytes(blob))
        self.assertEqual(count, 7)
        self.assertEqual(next_seq, 8)
        self.assertEqual(committed, len(blob))

    def test_uncommitted_tail_is_reported_not_parsed(self):
        blob = build_scripted_fixture() + b"\xde\xad\xbe\xef" * 8
        mlg = MlgFile.parse(blob)
        self.assertEqual(len(mlg.events), 7)
        self.assertEqual(mlg.uncommitted_tail, 32)


class TestLargeFile(unittest.TestCase):
    def test_total_length_crosses_64_kib(self):
        blob = build_large_fixture()
        self.assertGreater(len(blob), 0x10000)
        mlg = MlgFile.parse(blob)
        self.assertGreater(mlg.events[-1].offset, 0x10000)
        self.assertEqual(mlg.header.committed_length, len(blob))
        # Every offset must be reachable by the backwards chain too.
        cur = mlg.events[-1]
        steps = 0
        while cur.prev_offset:
            cur = next(e for e in mlg.events if e.offset == cur.prev_offset)
            steps += 1
        self.assertEqual(steps, len(mlg.events) - 1)


class TestMappingFingerprint(unittest.TestCase):
    def test_fingerprint_is_deterministic_and_order_independent(self):
        mapping = load_mapping()
        fp = mapping_fingerprint(mapping)
        shuffled = {"char_to_id": dict(reversed(list(mapping["char_to_id"].items())))}
        self.assertEqual(mapping_fingerprint(shuffled), fp)

    def test_fingerprint_changes_when_a_glyph_moves(self):
        mapping = load_mapping()
        fp = mapping_fingerprint(mapping)
        c2i = dict(mapping["char_to_id"])
        a, b = list(c2i)[0], list(c2i)[1]
        c2i[a], c2i[b] = c2i[b], c2i[a]
        self.assertNotEqual(mapping_fingerprint({"char_to_id": c2i}), fp)

    def test_python_constant_matches_the_generated_mapping(self):
        self.assertEqual(mapping_fingerprint(load_mapping()), MSGLOG_MAPPING_FINGERPRINT)

    def test_c_header_constant_is_in_sync(self):
        if not MSGLOG_H.exists():
            self.skipTest("engine submodule not checked out")
        text = MSGLOG_H.read_text(encoding="utf-8")
        m = re.search(r"#define\s+MSGLOG_MAPPING_FINGERPRINT\s+0x([0-9A-Fa-f]+)UL", text)
        self.assertIsNotNone(m, "MSGLOG.H must pin the mapping fingerprint")
        self.assertEqual(int(m.group(1), 16), MSGLOG_MAPPING_FINGERPRINT)


class TestCHeaderConstantsInSync(unittest.TestCase):
    """The Python codec and the DOS core must agree on every format constant."""

    NAME_MAP = {
        "MSGLOG_FORMAT_VERSION": MLG_FORMAT_VERSION,
        "MSGLOG_HEADER_SIZE": MLG_HEADER_SIZE,
        "MSGLOG_EVENT_HEAD_SIZE": MLG_EVENT_HEAD_SIZE,
        "MSGLOG_MAX_SPEAKER": 64,
        "MSGLOG_MAX_LOCATION": 64,
        "MSGLOG_MAX_BODY": MLG_MAX_BODY,
        "MSGLOG_KIND_CONV_BEGIN": MLG_KIND_CONV_BEGIN,
        "MSGLOG_KIND_TEXT": MLG_KIND_TEXT,
        "MSGLOG_KIND_CHOICE": MLG_KIND_CHOICE,
        "MSGLOG_KIND_CONV_END": MLG_KIND_CONV_END,
        "MSGLOG_KIND_GAP": MLG_KIND_GAP,
        "MSGLOG_HF_SNAPSHOT": MLG_HF_SNAPSHOT,
        "MSGLOG_HF_HAS_GAP": MLG_HF_HAS_GAP,
        "MSGLOG_HF_SEALED": MLG_HF_SEALED,
        "MSGLOG_HF_DATA_CRC": MLG_HF_DATA_CRC,
        "MSGLOG_HF_GAM_BOUND": MLG_HF_GAM_BOUND,
        "MSGLOG_EV_CONTINUED": MLG_EV_CONTINUED,
        "MSGLOG_EV_MORE": MLG_EV_MORE,
    }

    def test_constants_match(self):
        if not MSGLOG_H.exists():
            self.skipTest("engine submodule not checked out")
        text = MSGLOG_H.read_text(encoding="utf-8")
        for name, expected in self.NAME_MAP.items():
            m = re.search(rf"#define\s+{name}\s+(0x[0-9A-Fa-f]+|\d+)", text)
            self.assertIsNotNone(m, f"{name} missing from MSGLOG.H")
            self.assertEqual(int(m.group(1), 0), expected, name)


class TestDiagnostics(unittest.TestCase):
    def test_dump_renders_utf8(self):
        import io

        from tools.text.message_log import _dump

        path = FIXTURES / "fixture_scripted.mlg"
        path.write_bytes(build_scripted_fixture())
        try:
            buf = io.StringIO()
            rc = _dump(path, None, buf)
            self.assertEqual(rc, 0)
            out = buf.getvalue()
            self.assertIn("納馮", out)
            self.assertIn("三山當鋪", out)
            self.assertIn("2026-09-06 13:45:08", out)
            self.assertIn("CONV_BEGIN", out)
            self.assertIn("GAP", out)
        finally:
            path.unlink(missing_ok=True)


if __name__ == "__main__":
    unittest.main()
