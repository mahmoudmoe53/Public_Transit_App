import os
import psycopg2
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash, check_password_hash


load_dotenv()


def get_db_connection():
    conn = psycopg2.connect(host=os.getenv('DB_HOST'),
                             database=os.getenv('DB_NAME'),
                             user=os.getenv('DB_USERNAME'),
                             password=os.getenv('DB_PASSWORD'))
    return conn


class Users:
    def __init__(self, get_db_connection):
        self.get_db_connection = get_db_connection

    def create(self, name, email, password):
        """Create a new user in the database."""
        hashed_password = generate_password_hash(password)  
        connection = self.get_db_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("""
                INSERT INTO users (name, email, password)
                VALUES (%s, %s, %s)
            """, (name, email, hashed_password))
            connection.commit()
        except Exception as e:
            connection.rollback()
            print(f"Error creating user: {e}")
        finally:
            cursor.close()
            connection.close()

    def login(self, email, password):
        """Authenticate a user by comparing the provided password with the hashed password stored in the database."""
        connection = self.get_db_connection()
        cursor = connection.cursor()

        try:
            cursor.execute("SELECT id, name, password FROM users WHERE email = %s", (email,))
            user = cursor.fetchone()

            
            if user and check_password_hash(user[2], password):  
                return user  
            else:
                return None
        except Exception as e:
            print(f"Error logging in user: {e}")
            return None
        finally:
            cursor.close()
            connection.close()
