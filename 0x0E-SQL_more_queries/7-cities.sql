-- Creates database with cities table in it
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
id INT NOT NULL AUTO_INCREMENT,
state_id, INT NOT NULL FOREIGN KEY(statesid),
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id)
);
