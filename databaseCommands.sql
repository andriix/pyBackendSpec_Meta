-- MySQL terminal commands ->
mysql;

-- LABS
create database cm_devices;
--------
use cm_devices;
show columns from devices;

-- CREATE statement
CREATE TABLE devices (deviceID int, deviceName varchar(50), price decimal);

CREATE TABLE feedback(feedbackID CHAR(8), feedbackType VARCHAR(100),
                      comment TEXT(500));
CREATE TABLE Address (id int NOT NULL,  street VARCHAR(255),
                      postcode VARCHAR(10) DEFAULT "HA97DE",
                      town VARCHAR(30) DEFAULT "Harrow");

-- ALTER statement
ALTER TABLE devices ADD (deviceType varchar(50), deviceSize varchar(10));

ALTER TABLE devices DROP COLUMN deviceType;

ALTER TABLE devices MODIFY deviceName varchar(100);

-- INSERT statement
INSERT INTO devices(deviceID, deviceName, price) VALUES (123, "Samsung M32", 250),
                                                        (124, "Apple 14", 800)
INSERT INTO target_table(column_name) SELECT column_name FROM source_table;
-- SELECT statement
SELECT deviceName FROM devices;

SELECT deviceName, price FROM devices;

SELECT * FROM devices;
