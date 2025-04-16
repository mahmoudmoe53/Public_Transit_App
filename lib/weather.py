import requests 
import os
from dotenv import load_dotenv

load_dotenv()
secret_key = os.environ.get("WEATHER_API_KEY")

class Weather:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


    def location_weather(self):
        response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={self.lat}&lon={self.lon}&exclude=hourly,daily&appid={secret_key}")
        if response.status_code == 200:
            return response.json()
        else:
            return "Could Not Find Weather Information"