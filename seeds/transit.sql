DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users;

CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);



INSERT INTO users (name, email, password) VALUES ('Mahmoud', 'mahmoud@gmail.com', 'password123');
INSERT INTO users (name, email, password) VALUES ('Abdirahman', 'Abdirahman@gmail.com', 'password123');
INSERT INTO users (name, email, password) VALUES ('Ali', 'Ali@gmail.com', 'password123');
INSERT INTO users (name, email, password) VALUES ('Shaker', 'Shaker@gmail.com', 'password123');