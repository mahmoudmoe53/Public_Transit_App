import os
import psycopg2
from flask import Flask, render_template, request, jsonify, session, url_for, redirect
from dotenv import load_dotenv
from lib.users import Users, get_db_connection
import requests
from lib.gpsApi import Gps
from lib.googleApi import GoogleApi
from lib.tflApi import TflApi
from lib.tomtomApi import TomtomApi
from lib.weather import Weather

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_KEY")

def get_db_connection():
    conn = psycopg2.connect(host=os.getenv('DB_HOST'),
                            database=os.getenv('DB_NAME'),
                            user=os.getenv('DB_USERNAME'),
                            password=os.getenv('DB_PASSWORD'))
    return conn

users = Users(get_db_connection)

USER_IP_URL = "http://ip-api.com/json/"


def is_logged_in():
    return "user_id" in session

@app.route('/', methods=['GET', 'POST'])
def hello():
    if not is_logged_in():
        return redirect(url_for('login'))
    
    gps = Gps()
    gps.get_location()
    session['lat'] = gps.latitude
    session['lon'] = gps.longitude
    
    location = None
    if request.method == "POST":
        location = request.form.get("location")
    
    if not location:
        return render_template('index.html')

    lat = session.get('lat')
    lon = session.get('lon')

    startend = GoogleApi(lat, lon, location)
    startend.get_start_end_point()
    destination = startend.stop_location()
    bus_stop_name = startend.remove_after_bracket(destination)
    bus_stop_letter = startend.stop_letter(destination)

    testing_arrivals = TflApi()
    parent_number = testing_arrivals.get_parent_number(bus_stop_name)
    child_number = testing_arrivals.get_child_number(parent_number, bus_stop_letter)
    arrivals = testing_arrivals.get_live_arrivals(child_number)

    testing_update = TomtomApi(lat, lon)
    cc = testing_update.get_coordinates()
    pp = testing_update.get_accident_update(cc)

    weather = Weather(lat=lat, lon=lon)
    temps = weather.location_weather()

    return render_template("index.html", temps=temps, arrivals=arrivals)

@app.route("/signup", methods=['GET', 'POST'])
def sign_up():
    if is_logged_in():
        return redirect(url_for('hello'))

    if request.method == 'GET':
        return render_template("signup.html")

    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    if not name or not email or not password:
        return jsonify({"error": "All fields (name, email, password) are required"}), 400

    users.create(name, email, password)
    return jsonify({"message": "User created successfully"}), 201

@app.route("/login", methods=['GET', 'POST'])
def login():
    if is_logged_in():
        return redirect(url_for('hello'))

    if request.method == 'GET':
        return render_template("login.html")
    
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"error": "Both fields required"}), 400

    user = users.login(email, password)
    
    if user:
        session["user_id"] = user[0]  
        session["user_name"] = user[1]  
        return redirect(url_for('hello'))  
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
