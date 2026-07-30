-- creates the database hbtn_0d_usa if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- creates the table states if it doesn't already exist
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
