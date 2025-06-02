import pytest
import os
import psycopg2
from unittest.mock import Mock, patch
from lib.init_db import get_db_connection

@pytest.fixture
def mock_env_vars():
    "Mock environment variables for testing."
    with patch.dict(os.environ, {
        'WEATHER_API_KEY': 'test_weather_key',
        'API_KEY': 'test_google_key',
        'TOMTOM_API_KEY': 'test_tomtom_key',
        'DB_HOST': 'localhost',
        'DB_NAME': 'test_db',
        'DB_USERNAME': 'test_user',
        'DB_PASSWORD': 'test_pass'
    }):
        yield

@pytest.fixture
def mock_requests():
    "Mock requests module."
    with patch('requests.get') as mock_get:
        yield mock_get

@pytest.fixture
def mock_db_connection():
    "Mock database connection."
    mock_conn = Mock()
    mock_cursor = Mock()
    mock_conn.cursor.return_value = mock_cursor
    
    with patch('lib.users.get_db_connection', return_value=mock_conn):
        yield mock_conn, mock_cursor