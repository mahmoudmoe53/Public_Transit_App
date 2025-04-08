import os
import psycopg2
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from lib.users_repository import UsersRepository
import requests 

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host=os.getenv('DB_HOST'),
                            database=os.getenv('DB_NAME'),
                            user=os.getenv('DB_USERNAME'),
                            password=os.getenv('DB_PASSWORD'))
    return conn

users = UsersRepository(get_db_connection())

USER_IP_URL = "http://ip-api.com/json/"






# @app.route("location")
# def location():

@app.route('/', methods=['GET'])
def get_location():
    # Get the user's IP address
    # user_ip = request.remote_addr

    # Make a request to the ip-api geolocation service
    response = requests.get(f'http://ip-api.com/json/81.153.29.244')
    
    if response.status_code == 200:
        data = response.json()
        latitude = data.get('lat')
        longitude = data.get('lon')
        
        if latitude and longitude:
            return jsonify({
                'ip': "81.153.29.244",
                'latitude': latitude,
                'longitude': longitude
            })
        else:
            return jsonify({"error": "Location data not available."}), 400
    else:
        return jsonify({"error": "Could not fetch location data."}), 500




# @app.route("/")
# def index():
#     user = users.get_all_users()

#     return render_template('index.html', users=user)












if __name__ == "__main__":
    app.run(debug=True)