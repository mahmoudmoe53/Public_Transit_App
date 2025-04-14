import requests
import os
from flask import jsonify
from lib.gps import Gps
from dotenv import load_dotenv

load_dotenv()
secret_key = os.environ.get("API_KEY")

class GoogleApi(Gps):
    def __init__(self, latitude, longitude, destination):
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.destination = destination

    def get_start_end_point(self):
        origin = f"{self.latitude},{self.longitude}"
        destination = self.destination

        response = requests.get(
            f'https://maps.googleapis.com/maps/api/directions/json'
            f'?origin={origin}&destination={destination}&key={secret_key}'
        )

        if response.status_code == 200:
            a = response.json()
            return {
                "start_point": a["routes"][0]["legs"][0]["start_address"],
                "end_point": a["routes"][0]["legs"][0]["end_address"]
            }
        else:
            return {"error": "Could not fetch directions"}
