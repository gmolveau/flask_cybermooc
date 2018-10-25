# tests/test_1_database.py

from app.database import db

def test_db_tables(client):
    assert len(db.metadata.sorted_tables) == 3
    tables = ["users", "roles", "user_roles"]
    assert all(table in [t.name for t in db.metadata.sorted_tables] for table in tables)