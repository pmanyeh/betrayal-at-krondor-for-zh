import unittest
import re
from pathlib import Path

from tools.text.message_log_sources import OUTPUT, is_excluded, load_policy, render


class MessageLogSourcePolicyTests(unittest.TestCase):
    def test_generated_classifier_is_current(self):
        self.assertEqual(OUTPUT.read_text(encoding="ascii"), render())

    def test_known_transactions_and_system_messages_are_excluded(self):
        for key in (11, 14, 31, 35, 79, 81, 86, 107, 110, 153, 199, 216, 236, 245, 254, 269, 303, 315, 325, 329, 334, 336, 1300062, 1300083, 1800001, 1800048, 2100288, 2100291):
            self.assertTrue(is_excluded(key), key)

    def test_story_sources_remain_included(self):
        for key in (97, 1300001, 1600006, 2000023):
            self.assertFalse(is_excluded(key), key)

    def test_policy_keeps_unresolved_categories_explicit(self):
        self.assertEqual(load_policy()["unresolved"], [])

    def test_all_literal_combat_spell_and_puzzle_calls_are_excluded(self):
        root = Path(__file__).resolve().parents[2] / "upstream/betrayal-at-krondor/bak/SRC"
        files = sorted((root / "COMBAT").rglob("*.C"))
        files.extend([root / "SCREENS/CIPHER.C", root / "SCREENS/PICKLOCK.C"])
        pattern = re.compile(r"dialog_play_record\(\s*(0x[0-9a-f]+|[0-9]+)L?\s*,", re.I)
        found = []
        for path in files:
            found.extend(int(value, 0) for value in pattern.findall(path.read_text(encoding="latin1")))
        self.assertGreater(len(found), 40)
        self.assertEqual([key for key in found if not is_excluded(key)], [])


if __name__ == "__main__":
    unittest.main()
