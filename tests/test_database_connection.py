import os
import pytest
import psycopg2
from lib.init_db import get_db_connection, initialize_db

@pytest.fixture(scope='module')
def db_conn():
    conn = get_db_connection()
    yield conn
    conn.close()

def test_get_db_connection_succeeds(db_conn):
    cur = db_conn.cursor()
    cur.execute('SELECT version();')
    version_string = cur.fetchone()[0]
    cur.close()

    assert 'PostgreSQL' in version_string

def test_initialize_db_creates_users_table(db_conn):
    cur = db_conn.cursor()
    cur.execute('DROP TABLE IF EXISTS users;')
    db_conn.commit()
    cur.close()

    initialize_db()

    cur = db_conn.cursor()
    cur.execute("""
        SELECT column_name, data_type
          FROM information_schema.columns
         WHERE table_name = 'users';
    """)
    cols = {row[0]: row[1] for row in cur.fetchall()}
    cur.close()

    expected = {
        'id':       'integer',
        'name':     'character varying',
        'email':    'character varying',
        'password': 'character varying'
    }

    for col, dtype in expected.items():
        assert col in cols,      f"Missing column {col}"
        assert cols[col] == dtype, f"Column {col} should be {dtype}, got {cols[col]}"
