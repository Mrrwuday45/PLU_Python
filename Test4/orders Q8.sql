
CREATE DATABASE OrdersDB;
USE OrdersDB;

CREATE TABLE Orders (
    OrderID INT,
    CustomerName VARCHAR(100),
    OrderDate DATE,
    Amount INT
);

CREATE INDEX idx_OrderID
ON Orders(OrderID);
SHOW TABLES;
DESC Orders;
SHOW INDEX FROM Orders;