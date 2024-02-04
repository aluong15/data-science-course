CREATE TABLE sales (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(255),
    quantity_sold INT,
    unit_price DECIMAL(10, 2)
);

INSERT INTO sales VALUES
(1, 'Product A', 100, 10.50),
(2, 'Product B', 150, 15.75),
(3, 'Product C', 80, 8.99),
(4, 'Product D', 120, 12.25),
(5, 'Product E', 200, 18.50);

-- Count the number of products sold
SELECT COUNT(product_id) AS total_products_sold FROM sales;

-- Calculate the total quantity of products sold
SELECT SUM(quantity_sold) AS total_quantity_sold FROM sales;

-- Find the average unit price of the products
SELECT AVG(unit_price) AS avg_price FROM sales;

-- Get the total revenue generated from sales
SELECT SUM(quantity_sold * unit_price) AS total_revenue FROM sales;

-- Find the product with the highest quantity sold
SELECT product_name, quantity_sold FROM sales
ORDER BY quantity_sold DESC LIMIT 1;

SELECT product_name, quantity_sold
FROM sales
WHERE quantity_sold = (SELECT MAX(quantity_sold) FROM sales);
