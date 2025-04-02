import psycopg2
class UsersRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def get_all_users(self):
        with self.db_connection.cursor() as cursor:
            cursor.execute('SELECT * FROM users;')
            user = cursor.fetchall()
            cursor.close()
        return user


