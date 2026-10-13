from __future__ import annotations

import sys
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPTS_DIR = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS_DIR))

import archive_notes


class ArchiveNotesTest(unittest.TestCase):
    def test_ingest_is_disabled_unless_explicitly_enabled(self) -> None:
        with patch.object(archive_notes, "setting", return_value=""):
            self.assertFalse(archive_notes.ingest_enabled())

        with patch.object(archive_notes, "setting", return_value="true"):
            self.assertTrue(archive_notes.ingest_enabled())

    def test_disabled_ingest_does_not_read_brief_or_write_memora(self) -> None:
        with patch.object(archive_notes, "ingest_enabled", return_value=False):
            with patch.object(archive_notes, "BRIEFS_DIR", Path("/path/that/does/not/exist")):
                self.assertEqual(archive_notes.archive_brief("2026-08-25"), [])
            self.assertEqual(archive_notes.archive_candidates("2026-08-25", []), [])


if __name__ == "__main__":
    unittest.main()
