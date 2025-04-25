import psycopg2
from dotenv import load_dotenv
import os
import bcrypt

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
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cur = self.db_connection.cursor()
        cur.execute(
            'INSERT INTO users (name, email, password) VALUES (%s, %s, %s)',
            (name, email, hashed_password)
        )
        self.db_connection.commit()
        cur.close()
        

    def authenticate(self, email, password):
        cur = self.db_connection.cursor()
        cur.execute('SELECT password FROM users WHERE email = %s', (email,))
        row = cur.fetchone()
        cur.close()

        if row is None:
            return False  

        stored_hashed_password = row[0].encode('utf-8')  

        return bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password)
    


