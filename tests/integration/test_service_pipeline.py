import sqlite3
from unittest.mock import AsyncMock, patch

import pytest

from etl_service_pipeline.service import run_etl_pipeline


@pytest.mark.asyncio
async def test_run_etl_pipeline_end_to_end(tmp_path):
    db_path = tmp_path / "etl_integration.db"

    fake_data = [
        [{"id": "1", "name": " Alice ", "value": "20"}],
        [{"id": "2", "name": "Bob ", "value": "30"}],
    ]

    # Mock extract_from_sources to return fake API data
    with patch(
        "etl_service_pipeline.service.extract_from_sources",
        AsyncMock(return_value=fake_data),
    ):
        await run_etl_pipeline(
            ["https://fake.api/1", "https://fake.api/2"], str(db_path)
        )

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items;")
    rows = cursor.fetchall()
    conn.close()

    assert len(rows) == 2
    assert rows[0][1].strip() == "Alice"
    assert rows[1][2] == 30.0
