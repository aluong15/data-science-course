CREATE TABLE orders (
	order_id INT AUTO_INCREMENT PRIMARY KEY,
	customer_id INT,
    product_name VARCHAR(50),
    quantity INT,
    total_amount INT
);
CREATE TABLE customers (
	customer_id INT,
    customer_name VARCHAR(50),
	city VARCHAR(50)
);

INSERT orders (order_id, customer_id, product_name, quantity, total_amount) VALUES 
    (1, 101, "Laptop", 2, 2000),
    (2, 102, "Smartphone", 1, 800),
    (3, 103, "Headphones", 3, 150),
    (4, 101, "Tablet", 1, 500),
    (5, 104, "Smartwatch", 2, 300);
    
INSERT customers (customer_id, customer_name, city) VALUES 
    (101, "John Smith", "New York"),
    (102, "Jane Doe", "Los Angeles"),
    (103, "Robert Brown", "Chicago"),
    (104, "Emily White", "Houston");

-- Write a SQL query to retrieve the details of orders with a total amount greater than $500.
-- Use a subquery to find the customers who have placed orders with a total amount greater than $500.
-- Write a query to display the customer name, city, and the total number of orders they have placed.
-- Use a subquery to find the customer(s) who placed the maximum quantity order.

SELECT * FROM orders WHERE total_amount > 500;

SELECT customer_id FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders WHERE total_amount > 500);

SELECT c.customer_name, c.city, o.total_amount
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
ORDER BY c.customer_name ASC;

SELECT MAX(quantity) FROM orders;
-- SELECT customer_id, customer_name
-- FROM customers
-- WHERE customer_id IN (SELECT customer_id FROM orders ORDER BY quantity DESC LIMIT 1)

SELECT c.customer_id, c.customer_name
FROM customers c
JOIN (
	SELECT customer_id
    FROM orders 
    ORDER BY quantity DESC LIMIT 1) o
ON c.customer_id = o.customer_id;