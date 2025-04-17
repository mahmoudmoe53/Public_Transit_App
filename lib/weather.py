import requests 
import os
from dotenv import load_dotenv

CONVERSION = 273.15

load_dotenv()
secret_key = os.environ.get("WEATHER_API_KEY")

class Weather:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon


    def location_weather(self):
        
        '''This is a methods that takes the arrival destination and returns the current temperature'''
        
        response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?lat={self.lat}&lon={self.lon}&exclude=hourly,daily&appid={secret_key}")
        if response.status_code == 200:
            data = response.json()
            kelvin = data.get("current", {}).get("temp", "couldn't find temp")
            final_temp = round(kelvin - CONVERSION)
            return f"{final_temp}°C"

        else:
            return "Could Not Find Weather Information"