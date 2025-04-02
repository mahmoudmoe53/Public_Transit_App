import os
import psycopg2
from flask import Flask, render_template
from dotenv import load_dotenv
from lib.users_repository import UsersRepository

load_dotenv()

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host=os.getenv('DB_HOST'),
                            database=os.getenv('DB_NAME'),
                            user=os.getenv('DB_USERNAME'),
                            password=os.getenv('DB_PASSWORD'))
    return conn

users = UsersRepository(get_db_connection())

@app.route("/")
def index():
    user = users.get_all_users()

    return render_template('index.html', users=user)










if __name__ == "__main__":
    app.run(debug=True)