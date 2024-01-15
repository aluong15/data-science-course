CREATE TABLE products (
	order_id INT AUTO_INCREMENT PRIMARY KEY,
	product_name VARCHAR(255),
    customer VARCHAR(50)
);
CREATE TABLE customer_location (
	customer VARCHAR(50),
    location VARCHAR(50)
);

INSERT products (order_id, product_name, customer) VALUES 
    (1, 'Laptop', 'John'),
    (2, 'Smartphone', 'Alice'),
    (3, 'Tablet', 'Bob'),
    (4, 'Printer', 'David');
    
INSERT customer_location (customer, location) VALUES 
    ('John', 'New York'),
    ('Alice', 'California'),
    ('Bob', 'Texas'),
    ('Eve', 'Florida');

-- Inner Join:
-- Select Orders.OrderID, Orders.Product, Orders.Customer, and Customers.Location.
-- Include a condition in the ON clause to match the Customer between the two tables.
-- Left Join:
-- Select Orders.OrderID, Orders.Product, Orders.Customer, and Customers.Location.
-- Include a condition in the ON clause to match the Customer between the two tables.
-- Include all rows from the Orders table.
-- Right Join:
-- Select Orders.OrderID, Orders.Product, Orders.Customer, and Customers.Location.
-- Include a condition in the ON clause to match the Customer between the two tables.
-- Include all rows from the Customers table.

SELECT products.order_id, products.product_name, products.customer, customer_location.location
FROM products
INNER JOIN customer_location
ON products.customer = customer_location.customer;
 
SELECT products.order_id, products.product_name, products.customer, customer_location.location
FROM products
LEFT JOIN customer_location
ON products.customer = customer_location.customer;

SELECT products.order_id, products.product_name, products.customer, customer_location.location
FROM products
RIGHT JOIN customer_location
ON products.customer = customer_location.customer;
