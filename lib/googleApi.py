import requests
import os
from flask import jsonify
from lib.gpsApi import Gps
from dotenv import load_dotenv

load_dotenv()
secret_key = os.environ.get("API_KEY")

class GoogleApi(Gps):
    def __init__(self, latitude, longitude, destination):
        super().__init__()
        self.latitude = latitude
        self.longitude = longitude
        self.destination = destination
        # self.stop_name = 17
        # self.stop_letter = 0

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
            return a["routes"][0]["legs"][0]["steps"][1]["transit_details"]["departure_stop"]["name"]
            
        else:
            return {"error": "Could not fetch directions"}
        
        
    def remove_after_bracket(self, input_string):
        index = input_string.find('(')
        
        if index != -1:
            return input_string[:index].strip()
        else:
            return input_string.strip()
        
    def stop_letter(self, input_string):
        start_index = input_string.find('(')
        end_index = input_string.find(')')
        
        # If both '(' and ')' are found, extract the content between them
        if start_index != -1 and end_index != -1 and end_index > start_index:
            return input_string[start_index + 1:end_index].strip()
        else:
            return ""

        
    



        