-- script that creates a table users with the following fields
-- id (integer, never null, auto increment and primary key), email, name (never null and unique)
CREATE TABLE IF NOT EXISTS users (
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255)
)
