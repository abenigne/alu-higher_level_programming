-- Lists all privileges of the MySQL users user_0d_1 and user_0d_2 on localhost.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
CREATE DATABASE IF NOT EXISTS user_2_db;
GRANT SELECT, INSERT ON user_2_db.* TO 'user_0d_2'@'localhost';

SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
