CREATE DATABASE IF NOT EXIST contacts_manager

CREATE TABLE IF NOT EXIST contacts (
    id: INT AUTOINCREMENT PRIMRY KEY,
    first_name: VARCHAR(50) NOT NULL,
    last_name: VARCHAR(50) NOT NULL,
    phone_number: VARCHAR(20) NOT NULL
)