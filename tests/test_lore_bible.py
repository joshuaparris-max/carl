import unittest

from src.data_loader import load_json


class LoreBibleTests(unittest.TestCase):
    def setUp(self):
        self.lore = load_json("lore_bible.json")

    def test_all_entries_use_known_status_and_risk_labels(self):
        statuses = set(self.lore["status_labels"])
        risks = set(self.lore["legal_risk_labels"])
        for entry in self.lore["entries"]:
            self.assertIn(entry["canon_status"], statuses, entry["id"])
            self.assertIn(entry["legal_risk"], risks, entry["id"])

    def test_all_entries_have_design_translation(self):
        for entry in self.lore["entries"]:
            self.assertTrue(entry["source"], entry["id"])
            self.assertTrue(entry["gameplay_translation"], entry["id"])


if __name__ == "__main__":
    unittest.main()
