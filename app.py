import os
import psycopg2
from flask import Flask, render_template

from lib.users_repository import UsersRepository

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='transit_tracker',
                            user=os.environ['DB_USERNAME'],
                            password=os.environ['DB_PASSWORD'])
    return conn

users = UsersRepository(get_db_connection)

@app.route("/")
def index():
    user = users.get_all_users()

    render_template('index.html', users=user)








if __name__ == "__main__":
    app.run(debug=True)