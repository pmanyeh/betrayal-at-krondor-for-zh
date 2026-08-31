import unittest

from tools.release import bspatch_apply as bp


class TestInt64Codec(unittest.TestCase):
    def test_round_trip_matches_bsdiff_reference_values(self):
        # Reference (value -> 8-byte little-endian magnitude+sign) pairs
        # cross-checked against bsdiff4.core.{encode,decode}_int64.
        cases = [
            (0, b"\x00" * 8),
            (1, b"\x01" + b"\x00" * 7),
            (-1, b"\x01" + b"\x00" * 6 + b"\x80"),
            (255, bytes([255, 0, 0, 0, 0, 0, 0, 0])),
            (-255, bytes([255, 0, 0, 0, 0, 0, 0, 0x80])),
        ]
        for value, encoded in cases:
            self.assertEqual(bp.decode_int64(encoded), value)


class TestApplyPatch(unittest.TestCase):
    def test_apply_patch_reproduces_target_bsdiff4_reference(self):
        bsdiff4 = self._require_bsdiff4()
        src = b"The quick brown fox jumps over the lazy dog. " * 50
        dst = (b"The quick BROWN fox leaps over the lazy dog! " * 50) + b"extra tail bytes"
        patch_bytes = bsdiff4.diff(src, dst)
        result = bp.apply_patch(src, patch_bytes)
        self.assertEqual(result, dst)

    def test_bad_magic_raises(self):
        with self.assertRaises(ValueError):
            bp.apply_patch(b"anything", b"NOTAPATCH" + b"\x00" * 32)

    @staticmethod
    def _require_bsdiff4():
        try:
            import bsdiff4
        except ImportError:
            raise unittest.SkipTest("bsdiff4 not installed (dev-only dependency for patch generation)")
        return bsdiff4


if __name__ == "__main__":
    unittest.main()
