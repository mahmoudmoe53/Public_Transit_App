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
            f'?origin={origin}&destination={destination}&key={secret_key}&mode=transit&transit_mode=bus'
        )

        if response.status_code == 200:
            a = response.json()
            return {
                "start_point": a["routes"][0]["legs"][0]["start_address"],
                "end_point": a["routes"][0]["legs"][0]["end_address"],
                "time_taken": a["routes"][0]["legs"][0]["duration"]["text"]
            }
        else:
            return {"error": "Could not fetch directions"}


    def stop_location(self):
        origin = f"{self.latitude},{self.longitude}"
        destination = self.destination

        response = requests.get(
            f'https://maps.googleapis.com/maps/api/directions/json'
            f'?origin={origin}&destination={destination}&key={secret_key}&mode=transit&transit_mode=bus'
        )

        if response.status_code == 200:
            a = response.json()
            return {
                "departure_stop": a["routes"][0]["legs"][0]["steps"][1]["transit_details"]["departure_stop"]["name"]
            }
        else:
            return {"error": "Could not fetch directions"}


        