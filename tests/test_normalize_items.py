from __future__ import annotations

import sys
import unittest
from datetime import date
from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

from normalize_items import is_recent_item, item_local_date


class ItemDateFilterTest(unittest.TestCase):
    def test_keeps_run_date_and_previous_local_date(self) -> None:
        self.assertTrue(
            is_recent_item(
                {"published_at": "2026-08-12T00:30:00+00:00"},
                "2026-08-12",
            )
        )
        self.assertTrue(
            is_recent_item(
                {"published_at": "2026-08-10T16:30:00+00:00"},
                "2026-08-12",
            )
        )

    def test_excludes_older_or_future_items(self) -> None:
        self.assertFalse(
            is_recent_item(
                {"published_at": "2026-08-10T15:59:59+00:00"},
                "2026-08-12",
            )
        )
        self.assertFalse(
            is_recent_item(
                {"published_at": "2026-08-13T00:00:00+00:00"},
                "2026-08-12",
            )
        )

    def test_uses_fetched_at_when_published_at_is_missing(self) -> None:
        item = {"published_at": "", "fetched_at": "2026-08-12T01:00:00+00:00"}
        self.assertEqual(item_local_date(item), date(2026, 8, 12))
        self.assertTrue(is_recent_item(item, "2026-08-12"))
        self.assertFalse(
            is_recent_item(
                {"published_at": "", "fetched_at": "2026-08-11T01:00:00+00:00"},
                "2026-08-12",
            )
        )

    def test_invalid_or_missing_dates_are_excluded(self) -> None:
        self.assertIsNone(item_local_date({"published_at": "not-a-date"}))
        self.assertFalse(is_recent_item({"published_at": "not-a-date"}, "2026-08-12"))
        self.assertFalse(is_recent_item({}, "2026-08-12"))


if __name__ == "__main__":
    unittest.main()
