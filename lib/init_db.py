import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USERNAME'),
        password=os.getenv('DB_PASSWORD')
    )

def initialize_db():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS users;')

    cur.execute('CREATE TABLE users (id SERIAL PRIMARY KEY,'
                'name VARCHAR(255) NOT NULL,'
                'email VARCHAR(255) NOT NULL,'
                'password VARCHAR(255) NOT NULL);')

    conn.commit()
    cur.close()
    conn.close()




