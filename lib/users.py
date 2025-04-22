import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(host=os.getenv('DB_HOST'),
                            database=os.getenv('DB_NAME'),
                            user=os.getenv('DB_USERNAME'),
                            password=os.getenv('DB_PASSWORD'))

cur = conn.cursor()

class Users:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def create(self, name, email, password):
        cur = self.db_connection.cursor()
        cur.execute(
            'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
            (name, email, password)
        )
        self.db_connection.commit()
        cur.close()
        
    


