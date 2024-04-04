-- MySQL terminal commands ->
mysql;
-- LAB 1
create database cm_devices;

use cm_devices;
-- create statements
CREATE TABLE devices (deviceID int, deviceName varchar(50), price decimal);

CREATE TABLE feedback(feedbackID CHAR(8), feedbackType VARCHAR(100),
                      comment TEXT(500));
CREATE TABLE Address (id int NOT NULL,  street VARCHAR(255),
                      postcode VARCHAR(10) DEFAULT "HA97DE",
                      town VARCHAR(30) DEFAULT "Harrow");

show columns from devices;
-- alter statements
ALTER TABLE devices ADD (deviceType varchar(50), deviceSize varchar(10));

ALTER TABLE devices DROP COLUMN deviceType;

ALTER TABLE devices MODIFY deviceName varchar(100);
--------------------

