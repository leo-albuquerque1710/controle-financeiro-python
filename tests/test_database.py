
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import database


class DatabaseTests(unittest.TestCase):

    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_file = Path(self.temp_dir.name) / "test.db"

        self.path_patcher = patch.object(database, "DB_PATH", self.db_file)
        self.path_patcher.start()

        database.initialize_database()

    def tearDown(self):
        self.path_patcher.stop()
        self.temp_dir.cleanup()

    def test_add_and_list_transaction(self):
        new_id = database.add_transaction(
            "Salário", 2500.0, "receita",
            "trabalho", "2026-11-03"
        )

        rows = database.list_transactions()

        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["id"], new_id)
        self.assertEqual(rows[0]["description"], "Salário")

    def test_summary(self):
        database.add_transaction(
            "Salário", 2500, "receita",
            "trabalho", "2026-11-03"
        )

        database.add_transaction(
            "Aluguel", 900, "despesa",
            "moradia", "2026-11-03"
        )

        summary = database.get_summary()

        self.assertEqual(summary["income"], 2500)
        self.assertEqual(summary["expenses"], 900)
        self.assertEqual(summary["balance"], 1600)

    def test_delete_transaction(self):
        transaction_id = database.add_transaction(
            "Café", 10, "despesa",
            "alimentação", "2026-11-03"
        )

        self.assertTrue(database.delete_transaction(transaction_id))
        self.assertFalse(database.delete_transaction(transaction_id))
        self.assertEqual(database.list_transactions(), [])


if __name__ == "__main__":
    unittest.main()
