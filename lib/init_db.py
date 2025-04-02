import os
import psycopg2

conn = psycopg2.connect(host='localhost',
                        database='transit_tracker',
                        user=os.environ['DB_USERNAME'],
                        password=os.environ['DB_PASSWORD']

)

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



