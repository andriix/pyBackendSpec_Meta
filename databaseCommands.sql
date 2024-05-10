-- MySQL terminal commands ->
mysql;

-- LABS
create database cm_devices;
--------
use cm_devices;
show columns from devices;

-- CREATE statement
CREATE TABLE devices (deviceID int, deviceName varchar(50), price decimal);

CREATE TABLE accessories (accessID int, accessName varchar(50), device_id int,
                          PRIMARY KEY (accessID),
                          FOREIGN KEY (device_id) REFERENCES devices(deviceID)
                          )

CREATE TABLE feedbacks(feedbackID CHAR(8), feedbackType VARCHAR(100),
                      comment TEXT(500));
CREATE TABLE Addresses (id int NOT NULL,  street VARCHAR(255),
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

-- UPDATE statement
UPDATE devices SET price = 240 WHERE ID = 123

UPDATE Addresses SET postcode = "65012" WHERE town = "Odesa"

-- DELETE statement
DELETE FROM devices WHERE deviceName = "Sony WT19i"

-- ORDER BY clause
SELECT deviceName, price FROM devices ORDER BY deviceName ASC

-- WHERE clause
SELECT deviceName FROM devices WHERE price BETWEEN 100 and 200
SELECT deviceName FROM devices WHERE deviceName LIKE 'Asus TUF %'
SELECT * FROM Addresses WHERE town IN ('Odesa', 'Kyiv')























