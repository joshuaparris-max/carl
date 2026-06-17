import unittest

from src.announcements import AnnouncementManager
from src.data_loader import load_json


class AnnouncementTests(unittest.TestCase):
    def test_emit_formats_and_records_history(self):
        manager = AnnouncementManager(load_json("announcements.json"))
        line = manager.emit("welcome", crawler="Carl")
        self.assertIn("Carl", line)
        self.assertEqual(manager.history[-1], line)

    def test_unknown_announcement_returns_empty_string(self):
        manager = AnnouncementManager(load_json("announcements.json"))
        self.assertEqual(manager.emit("not_real"), "")


if __name__ == "__main__":
    unittest.main()
