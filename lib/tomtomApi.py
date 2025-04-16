import requests
from flask import jsonify
from lib.gpsApi import Gps
from dotenv import load_dotenv
import os

load_dotenv()
secret_key = os.environ.get("TOMTOM_API_KEY")

class TomtomApi:
    def __init__(self, longitude, latitude):
        self.longitude = longitude
        self.latitude = latitude

    
    def get_coordinates(self):
        min_cor = self.longitude - 0.009
        max_cor = self.longitude + 0.009
        min_lat = self.latitude - 0.015
        max_lat = self.latitude + 0.015
        return f'{min_cor},{min_lat},{max_cor},{max_lat}' 

    def get_accident_update(self, cor):
        response = requests.get(f'https://api.tomtom.com/traffic/services/5/incidentDetails?timeValidityFilter=present&key={secret_key}&bbox={cor}')
        
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Could not fetch update"}
    