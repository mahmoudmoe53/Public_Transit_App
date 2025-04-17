import requests
from flask import jsonify

class Gps:
    def __init__(self):
       self.latitude = 0  
       self.longitude = 0

    def get_location(self):

        '''methods that gets the current location using clients ip.\n (Currently using dummy data)'''

        response = requests.get('http://ip-api.com/json/81.153.29.244')
            
        if response.status_code == 200:
            data = response.json()
            self.latitude = data.get('lat')
            self.longitude = data.get('lon')
            
            if self.latitude and self.longitude:
                return jsonify({
                    'ip': "81.153.29.244",
                    'latitude': self.latitude,
                    'longitude': self.longitude
                })
            else:
                return jsonify({"error": "Location data not available."}), 400
        else:
            return jsonify({"error": "Could not fetch location data."}), 500

