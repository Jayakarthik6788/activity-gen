import csv
import tempfile
import unittest
from datetime import datetime
from pathlib import Path

from activity_gen import read_activities, record_activity


class ActivityGenTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.log_path = Path(self.temp_dir.name) / "activity_log.csv"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_records_entry_with_supplied_timestamp(self):
        timestamp = datetime(2026, 11, 23, 14, 30, 0)
        entry = record_activity(
            "activity-gen",
            "Add CSV logging",
            "Entry is saved",
            path=self.log_path,
            now=timestamp,
        )
        self.assertEqual(entry["date"], "2026-11-23")
        rows = read_activities(self.log_path)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["task"], "Add CSV logging")
        self.assertEqual(rows[0]["outcome"], "Entry is saved")

    def test_rejects_blank_project(self):
        with self.assertRaises(ValueError):
            record_activity("  ", "Do work", path=self.log_path)

    def test_rejects_blank_task(self):
        with self.assertRaises(ValueError):
            record_activity("activity-gen", "  ", path=self.log_path)

    def test_appends_multiple_entries(self):
        record_activity("project-a", "First task", path=self.log_path)
        record_activity("project-b", "Second task", path=self.log_path)
        self.assertEqual(len(read_activities(self.log_path)), 2)

    def test_csv_header_is_written_once(self):
        record_activity("project-a", "First task", path=self.log_path)
        record_activity("project-a", "Second task", path=self.log_path)
        with self.log_path.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.reader(handle))
        self.assertEqual(rows[0], ["date", "time", "project", "task", "outcome"])
        self.assertEqual(len(rows), 3)


if __name__ == "__main__":
    unittest.main()
