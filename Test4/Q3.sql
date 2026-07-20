create DATABASE products;
use products;
CREATE TABLE products (
    ProductID INT,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price INT
);
INSERT INTO products
VALUES
(1, 'Mouse', 'Electronics', 800),
(2, 'Laptop', 'Electronics', 65000),
(3, 'Chair', 'Furniture', 4500),
(4, 'Keyboard', 'Electronics', 1200);
SELECT * FROM products
WHERE Price > 1000;
SELECT * FROM products
WHERE Category = 'Electronics';
SELECT * FROM products
WHERE ProductName = 'Laptop';
