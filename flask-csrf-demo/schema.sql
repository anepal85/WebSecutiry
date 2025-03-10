CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL
);

INSERT INTO users (username, password, email) VALUES ('user1', 'pass1', 'user1@example.com');