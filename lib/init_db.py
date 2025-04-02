import os
import psycopg2
from dotenv import load_dotenv
load_dotenv()

conn = psycopg2.connect(host=os.getenv('DB_HOST'),
                            database=os.getenv('DB_NAME'),
                            user=os.getenv('DB_USERNAME'),
                            password=os.getenv('DB_PASSWORD'))



cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS users;')

cur.execute('CREATE TABLE users (id SERIAL PRIMARY KEY,'
            'name VARCHAR(255) NOT NULL,'
            'email VARCHAR(255) NOT NULL,'
            'password VARCHAR(255) NOT NULL);'
            )

cur.execute('INSERT INTO users (name, email, password)'
            'VALUES (%s, %s, %s)',
            ('Mahmoud', 'mahmoud@gmail.com', 'password123')
)

cur.execute('INSERT INTO users (name, email, password)'
            'VALUES (%s, %s, %s)',
            ('Abdirahman', 'abdirahman@gmail.com', 'password123')
)

cur.execute('INSERT INTO users (name, email, password)'
            'VALUES (%s, %s, %s)',
            ('Ali', 'ali@gmail.com', 'password123')
)

cur.execute('INSERT INTO users (name, email, password)'
            'VALUES (%s, %s, %s)',
            ('Shaker', 'shaker@gmail.com', 'password123')
)
conn.commit()

cur.close()
conn.close()



