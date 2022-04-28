DROP DATABASE IF EXISTS warehouse;
CREATE DATABASE IF NOT EXISTS warehouse;
use warehouse;

DROP TABLE IF EXISTS customers;
CREATE TABLE customers
(customerID INT PRIMARY KEY AUTO_INCREMENT,
firstName VARCHAR(15),
lastName VARCHAR(15),
email VARCHAR(30),
phoneNumber CHAR(10),
address VARCHAR(50)
);

DROP TABLE IF EXISTS employees;
CREATE TABLE employees
(employeeID INT PRIMARY KEY,
firstName VARCHAR(15),
lastName VARCHAR(15),
position VARCHAR(20),
phoneNumber CHAR(10),
address VARCHAR(50),
salary DOUBLE,
currentlyEmployed BOOL
);

DROP TABLE IF EXISTS injuryReports;
CREATE TABLE injuryReports
(injuryID INT PRIMARY KEY,
employeeID INT,
injuryDate DATE,
description VARCHAR(100),
FOREIGN KEY (employeeID) REFERENCES employees(employeeID)
);

DROP TABLE IF EXISTS products;
CREATE TABLE products
(productID INT PRIMARY KEY,
productName VARCHAR(50),
productPrice DOUBLE,
productNumberRemaining INT
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders
(orderID INT PRIMARY KEY,
customerID INT,
employeeID INT,
placedOn DATE,
fulfilledOn DATE,
notes VARCHAR(100),
FOREIGN KEY (customerID) REFERENCES customers(customerID),
FOREIGN KEY (employeeID) REFERENCES employees(employeeID)
);

DROP TABLE IF EXISTS orderItems;
CREATE TABLE orderItems
(orderID INT,
productID INT,
numberOrdered INT,
numberFulfilled INT,
PRIMARY KEY(orderID, productID),
FOREIGN KEY (orderID) REFERENCES orders(orderID),
FOREIGN KEY (productID) REFERENCES products(productID)
);