from lib.database_connection import DatabaseConnection

def test_database_connection():
    connection = DatabaseConnection()
    connection.connect()
    result = connection.execute("SELECT 1")
    assert result[0]["?column?"] == 1