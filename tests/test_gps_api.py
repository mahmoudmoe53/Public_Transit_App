import pytest
from unittest.mock import Mock, patch
from flask import Flask
from lib.gpsApi import Gps

class TestGps:
    
    @pytest.fixture
    def app(self):
        "Create Flask app for testing."
        app = Flask(__name__)
        return app
    
    @pytest.fixture
    def gps_instance(self):
        "Create Gps instance for testing."
        return Gps()
    
    def test_gps_init(self, gps_instance):
        "Test Gps class initialization."
        assert gps_instance.latitude == 0
        assert gps_instance.longitude == 0
    
    @patch('lib.gpsApi.requests.get')
    def test_get_location_success(self, mock_get, gps_instance, app):
        "Test successful location retrieval."
        with app.app_context():
            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                'lat': 51.5074,
                'lon': -0.1278
            }
            mock_get.return_value = mock_response
            
            result = gps_instance.get_location()
        
            assert gps_instance.latitude == 51.5074
            assert gps_instance.longitude == -0.1278
        
            mock_get.assert_called_once_with('http://ip-api.com/json/81.153.29.244')
    
    @patch('lib.gpsApi.requests.get')
    def test_get_location_api_failure(self, mock_get, gps_instance, app):
        "Test location API failure."
        with app.app_context():
            mock_response = Mock()
            mock_response.status_code = 500
            mock_get.return_value = mock_response
            
            result = gps_instance.get_location()
            
         
            assert result[1] == 500 
    
    @patch('lib.gpsApi.requests.get')
    def test_get_location_missing_data(self, mock_get, gps_instance, app):
        "Test location API with missing coordinate data."
        with app.app_context():

            mock_response = Mock()
            mock_response.status_code = 200
            mock_response.json.return_value = {
                'lat': None,
                'lon': None
            }
            mock_get.return_value = mock_response
            
            result = gps_instance.get_location()
            
            
            assert result[1] == 400 