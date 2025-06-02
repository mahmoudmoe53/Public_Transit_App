import pytest
from unittest.mock import Mock, patch
from lib.weather import Weather

class TestWeather:
    
    @pytest.fixture
    def weather_instance(self, mock_env_vars):
        "Create Weather instance for testing."
        return Weather(51.5074, -0.1278) 
    
    def test_weather_init(self, weather_instance):
        "Test Weather class initialization."
        assert weather_instance.lat == 51.5074
        assert weather_instance.lon == -0.1278
    
    @patch('lib.weather.requests.get')
    def test_location_weather_success(self, mock_get, weather_instance):
        "Test successful weather API call."
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "current": {
                "temp": 293.15 
            }
        }
        mock_get.return_value = mock_response
        
        result = weather_instance.location_weather()
        
        assert result == "20°C"
        mock_get.assert_called_once()
    
    @patch('lib.weather.requests.get')
    def test_location_weather_api_failure(self, mock_get, weather_instance):
        "Test weather API failure."
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response
        
        result = weather_instance.location_weather()
        
        assert result == "Could Not Find Weather Information"
    
    @patch('lib.weather.requests.get')
    def test_location_weather_negative_temp(self, mock_get, weather_instance):
        "Test weather with negative temperature."
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "current": {
                "temp": 263.15  
            }
        }
        mock_get.return_value = mock_response
        
        result = weather_instance.location_weather()
        
        assert result == "-10°C"