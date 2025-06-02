import pytest
from unittest.mock import Mock, patch
from datetime import datetime
from lib.tflApi import TflApi

class TestTflApi:
    
    @pytest.fixture
    def tfl_instance(self):
        return TflApi()
    
    @patch('lib.tflApi.requests.get')
    def test_get_parent_number_success(self, mock_get, tfl_instance):
        "Test successful parent number retrieval."
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "matches": [{
                "topMostParentId": "HUBKGX"
            }]
        }
        mock_get.return_value = mock_response
        
        result = tfl_instance.get_parent_number("King's Cross")
        
        assert result == "HUBKGX"
        mock_get.assert_called_once_with("https://api.tfl.gov.uk/StopPoint/Search/King's Cross")
    
    @patch('lib.tflApi.requests.get')
    def test_get_child_number_success(self, mock_get, tfl_instance):
        "Test successful child number retrieval."
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "children": [
                {
                    "stopLetter": "A",
                    "naptanId": "490000001A"
                },
                {
                    "stopLetter": "B",
                    "naptanId": "490000001B"
                }
            ]
        }
        mock_get.return_value = mock_response
        
        result = tfl_instance.get_child_number("HUBKGX", "A")
        
        assert result == "490000001A"
    
    @patch('lib.tflApi.requests.get')
    def test_get_child_number_with_stop_prefix(self, mock_get, tfl_instance):
        "Test child number retrieval with 'Stop' prefix."
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "children": [{
                "stopLetter": "A",
                "naptanId": "490000001A"
            }]
        }
        mock_get.return_value = mock_response
        
        result = tfl_instance.get_child_number("HUBKGX", "Stop A")
        
        assert result == "490000001A"
    
    @patch('lib.tflApi.requests.get')
    def test_get_child_number_not_found(self, mock_get, tfl_instance):
        "Test child number when stop letter not found."
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "children": [{
                "stopLetter": "A",
                "naptanId": "490000001A"
            }]
        }
        mock_get.return_value = mock_response
        
        result = tfl_instance.get_child_number("HUBKGX", "Z")
        
        assert result is None
    
    @patch('lib.tflApi.requests.get')
    def test_get_live_arrivals_success(self, mock_get, tfl_instance):
        "Test successful live arrivals retrieval."
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "expectedArrival": "2024-01-15T14:30:00Z"
            },
            {
                "expectedArrival": "2024-01-15T14:25:00Z"
            },
            {
                "expectedArrival": "2024-01-15T14:35:00Z"
            }
        ]
        mock_get.return_value = mock_response