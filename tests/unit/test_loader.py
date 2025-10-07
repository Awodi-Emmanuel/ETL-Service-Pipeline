import sqlite3

from etl_service_pipeline.loader import SQLiteLoader


def test_initialize_database_creates_table(tmp_path):
    db_path = tmp_path / "test.db"
    loader = SQLiteLoader(str(db_path))
    loader.initialize_database()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='items';"
    )
    result = cursor.fetchone()
    conn.close()

    assert result is not None


def test_load_records_inserts_data(tmp_path):
    db_path = tmp_path / "test.db"
    loader = SQLiteLoader(str(db_path))
    loader.initialize_database()
    records = [{"id": "1", "name": "Item1", "value": 10.5}]
    loader.load_records(records)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items;")
    rows = cursor.fetchall()
    conn.close()

    assert len(rows) == 1
    assert rows[0][1] == "Item1"
    assert rows[0][2] == 10.5
