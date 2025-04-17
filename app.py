import os
import psycopg2
from flask import Flask, render_template, request, jsonify, session
from dotenv import load_dotenv
from lib.users_repository import UsersRepository
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

users = UsersRepository(get_db_connection())

USER_IP_URL = "http://ip-api.com/json/"






# @app.route("location")
# def location():

@app.route('/', methods=['GET','POST'])
def hello():
    gps = Gps()
    gps.get_location()
    session['lat'] = gps.latitude
    session['lon'] = gps.longitude
    


    location = None
    if request.method == "POST":
        location = request.form.get("location")
    if not location:
        return render_template('results.html')

    lat = session.get('lat')
    print(lat)
    lon = session.get('lon')
    print(lon)


    startend = GoogleApi(lat, lon, location)
    a = startend.get_start_end_point() 
    b = startend.stop_location()
    bus_stop_name = startend.remove_after_bracket(b)
    print(bus_stop_name)
    bus_stop_letter = startend.stop_letter(b)
    print(bus_stop_letter)

    testing_arrivals = TflApi()
    aa = testing_arrivals.get_parent_number(bus_stop_name)
    bb = testing_arrivals.get_child_number(aa, bus_stop_letter)  # Add bus_stop_letter as the second argument
    print(bb)
    arrivals = testing_arrivals.get_live_arrivals(bb)
    print(arrivals)


    testing_update = TomtomApi(lat, lon)
    print(testing_update.latitude)
    cc = testing_update.get_coordinates()
    print(cc)
    pp = testing_update.get_accident_update(cc)
    print(pp)

    weather = Weather(lat=lat, lon=lon)
    temps = weather.location_weather()

    print(temps)
    
    return f"Temperature today is: {temps}\nThe bus timetable can be found below:\n{arrivals}"
    

# @app.route("/test", methods=['GET', 'POST'])





    return render_template('results.html', startend=a, message=a)

 









if __name__ == "__main__":
    app.run(debug=True)