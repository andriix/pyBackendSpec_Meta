-- MySQL terminal commands ->
mysql;
-- LAB 1
create database cm_devices;

use cm_devices;

CREATE TABLE devices (deviceID int, deviceName varchar(50), price decimal);

CREATE TABLE feedback(feedbackID CHAR(8), feedbackType VARCHAR(100),
                      comment TEXT(500));

show columns from devices;
--------------------

