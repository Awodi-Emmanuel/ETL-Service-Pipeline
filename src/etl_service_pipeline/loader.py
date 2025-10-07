import logging
import sqlite3
from typing import Dict, Iterable

logger = logging.getLogger(__name__)


class SQLiteLoader:
    """Handles loading normalized data into a SQLite database."""

    def __init__(self, db_path: str = "etl_service.db"):
        self.db_path = db_path

    def initialize_database(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS items (
                    id TEXT PRIMARY KEY,
                    name TEXT,
                    value REAL
                );
            """
            )
            conn.commit()
        logger.info(f"Database initialized: {self.db_path}")

    def load_records(self, records: Iterable[Dict]):
        records = list(records)
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            for rec in records:
                cur.execute(
                    "INSERT OR REPLACE INTO items (id, name, value) VALUES (?, ?, ?)",
                    (rec["id"], rec["name"], rec["value"]),
                )
            conn.commit()
        logger.info(f"{len(records)} records loaded into {self.db_path}")
