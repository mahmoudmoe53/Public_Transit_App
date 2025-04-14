import os
import psycopg2
from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
from lib.users_repository import UsersRepository
import requests 
from lib.gps import Gps
from lib.googleApi import GoogleApi


load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_KEY")

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
def hello():
    gps = Gps()
    gps.get_location()
    session['lat'] = gps.latitude
    session['lon'] = gps.longitude
    return "Location saved in session"

@app.route("/test", methods=['GET', 'POST'])
def google():

    location = None
    if request.method == "POST":
        location = request.form.get("location")
    if not location:
        return render_template('results.html')

    lat = session.get('lat')
    print(lat)
    lon = session.get('lon')
    print(location)


    startend = GoogleApi(lat, lon, location)
    a = startend.get_start_end_point()
    print(a)
    return render_template('results.html', startend=a, message=a)









if __name__ == "__main__":
    app.run(debug=True)