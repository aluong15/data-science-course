-- Create Customers Table
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(50),
    email VARCHAR(50),
    registration_date DATE
);

-- Insert Data into Customers Table
INSERT INTO customers (customer_id, customer_name, email, registration_date)
VALUES
    (1, 'Alice', 'alice@email.com', '2022-01-01'),
    (2, 'Bob', 'bob@email.com', '2022-02-15'),
    (3, 'Charlie', 'charlie@email.com', '2022-03-10');

-- Create Products Table
CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(50),
    price DECIMAL(10, 2)
);

-- Insert Data into Products Table
INSERT INTO products (product_id, product_name, category, price)
VALUES
    (101, 'Laptop', 'Electronics', 800.00),
    (102, 'Smartphone', 'Electronics', 500.00),
    (103, 'Headphones', 'Electronics', 100.00),
    (104, 'Coffee Maker', 'Appliances', 50.00);

-- Create Orders Table
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

-- Insert Data into Orders Table
INSERT INTO orders (order_id, customer_id, order_date)
VALUES
    (201, 1, '2022-01-05'),
    (202, 2, '2022-02-20'),
    (203, 3, '2022-03-15');

-- Create Order_Items Table
CREATE TABLE order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    total_price DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

-- Insert Data into Order_Items Table
INSERT INTO order_items (order_item_id, order_id, product_id, quantity, total_price)
VALUES
    (301, 201, 101, 2, 1600.00),
    (302, 201, 103, 1, 100.00),
    (303, 202, 102, 1, 500.00),
    (304, 203, 104, 3, 150.00);

-- Create Payments Table
CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    order_id INT,
    payment_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (order_id) REFERENCES orders(order_id)
);

-- Insert Data into Payments Table
INSERT INTO payments (payment_id, order_id, payment_date, amount)
VALUES
    (401, 201, '2022-01-06', 1700.00),
    (402, 202, '2022-02-25', 500.00),
    (403, 203, '2022-03-18', 150.00);

-- Basic Retrieval:
-- Write a SQL query to retrieve the total number of customers in the database.
SELECT COUNT(customer_id) FROM customers;
-- Write a query to get the product names and prices for products in the 'Electronics' category.
SELECT product_name, price, category
FROM products
WHERE category = "Electronics";

-- Joins:
-- Create a query to fetch the details of customers who made purchases, including their order details.
SELECT 
	cs.customer_id, 
    cs.customer_name, 
    o.order_id,
    o.order_date
FROM customers as cs
JOIN orders o ON cs.customer_id = o.customer_id;

-- Write a query to get the total revenue for each product category.
SELECT
	pr.product_id,
    pr.product_name,
    pr.category,
    oi.quantity,
    pr.price,
    oi.total_price
FROM
	products as pr
JOIN order_items oi ON pr.product_id = oi.product_id;

SELECT
	pr.category,
    SUM(oi.total_price) as total_revenue
FROM products as pr
JOIN order_items oi ON pr.product_id = oi.product_id
GROUP BY pr.category
ORDER BY total_revenue ASC;

-- Subqueries:
-- Use a subquery to find customers who made more than one order.
SELECT
	customer_id,
    order_count
FROM (
	SELECT 
		cs.customer_id,
		-- cs.customer_name,
		COUNT(o.order_id) as order_count
	--     oi.product_id
	FROM customers as cs
	JOIN orders o ON cs.customer_id = o.customer_id
	JOIN order_items oi ON o.order_id = oi.order_id
	GROUP BY cs.customer_id
) AS subquery
WHERE order_count > 1;

-- Write a query to display customers who made the highest total purchase amount.
SELECT
	cs.customer_id,
    cs.customer_name,
    -- COUNT(o.order_id) AS order_count,
    SUM(oi.total_price) AS total_purchase_amt
FROM customers as cs
JOIN orders o ON cs.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY cs.customer_id
ORDER BY total_purchase_amt DESC LIMIT 1;

-- Aggregate Functions:
-- Calculate the average order value for each customer.
SELECT
	cs.customer_id,
    cs.customer_name,
    COUNT(o.order_id) AS order_count,
    SUM(oi.total_price) AS total_purchase_amt,
    AVG(oi.total_price) AS avg_purchase_amt
FROM customers as cs
JOIN orders o ON cs.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY cs.customer_id;

-- Find the total revenue and average order value for each month.
SELECT 
	MONTH(payment_date) as payment_month,
    SUM(amount) as total_revenue,
    AVG(amount) as avg_order_value
FROM payments
GROUP BY payment_date;

-- Advanced Queries:
-- Identify the top 5 customers with the highest total purchase amount.
SELECT
	cs.customer_id,
    cs.customer_name,
    -- COUNT(o.order_id) AS order_count,
    SUM(oi.total_price) AS total_purchase_amt
FROM customers as cs
JOIN orders o ON cs.customer_id = o.customer_id
JOIN order_items oi ON o.order_id = oi.order_id
GROUP BY cs.customer_id
ORDER BY total_purchase_amt DESC LIMIT 5;

-- Write a query to find products that have not been ordered.
SELECT
	pr.product_id,
    pr.product_name,
    oi.quantity
FROM products as pr
LEFT JOIN order_items oi ON pr.product_id = oi.product_id
WHERE oi.product_id IS NULL
