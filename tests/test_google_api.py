import pytest
from unittest.mock import Mock, patch
from lib.googleApi import GoogleApi

class TestGoogleApi:
    
    @pytest.fixture
    def google_api_instance(self, mock_env_vars):
        "Create GoogleApi instance for testing."
        return GoogleApi(51.5074, -0.1278, "Oxford Circus")
    
    def test_google_api_init(self, google_api_instance):
        "Test GoogleApi class initialization."
        assert google_api_instance.latitude == 51.5074
        assert google_api_instance.longitude == -0.1278
        assert google_api_instance.destination == "Oxford Circus"
    
    @patch('lib.googleApi.requests.get')
    def test_get_start_end_point_success(self, mock_get, google_api_instance):
        "Test successful directions API call."
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "routes": [{
                "legs": [{
                    "start_address": "Test Start Address",
                    "end_address": "Test End Address",
                    "duration": {"text": "25 mins"}
                }]
            }]
        }
        mock_get.return_value = mock_response
        
        result = google_api_instance.get_start_end_point()
        
        assert result["start_point"] == "Test Start Address"
        assert result["end_point"] == "Test End Address"
        assert result["time_taken"] == "25 mins"
    
    @patch('lib.googleApi.requests.get')
    def test_get_start_end_point_failure(self, mock_get, google_api_instance):
        "Test directions API failure."
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response
        
        result = google_api_instance.get_start_end_point()
        
        assert "error" in result
        assert result["error"] == "Could not fetch directions"
    
    @patch('lib.googleApi.requests.get')
    def test_stop_location_success(self, mock_get, google_api_instance):
        "Test successful stop location retrieval."
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "routes": [{
                "legs": [{
                    "steps": [
                        {"travel_mode": "WALKING"},
                        {
                            "travel_mode": "TRANSIT",
                            "transit_details": {
                                "departure_stop": {
                                    "name": "Test Bus Stop (Stop A)"
                                }
                            }
                        }
                    ]
                }]
            }]
        }
        mock_get.return_value = mock_response
        
        result = google_api_instance.stop_location()
        
        assert result == "Test Bus Stop (Stop A)"
    
    def test_remove_after_bracket(self, google_api_instance):
        "Test bracket removal utility function."
        test_cases = [
            ("Test Stop (Stop A)", "Test Stop"),
            ("No Bracket Stop", "No Bracket Stop"),
            ("Multiple (Stop A) (Stop B)", "Multiple"),
            ("", "")
        ]
        
        for input_str, expected in test_cases:
            result = google_api_instance.remove_after_bracket(input_str)
            assert result == expected
    
    def test_stop_letter(self, google_api_instance):
        "Test stop letter extraction function."
        test_cases = [
            ("Test Stop (Stop A)", "Stop A"),
            ("Another Stop (B)", "B"),
            ("No Bracket", ""),
            ("Empty ()", ""),
            ("Multiple (A) (B)", "A")
        ]
        
        for input_str, expected in test_cases:
            result = google_api_instance.stop_letter(input_str)
            assert result == expected