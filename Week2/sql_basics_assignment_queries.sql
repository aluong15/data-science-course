CREATE TABLE IF NOT EXISTS products (
	product_id INT AUTO_INCREMENT PRIMARY KEY,
	product_name VARCHAR(255),
    price DECIMAL(10, 2),
    quantity_in_stock INT
);

INSERT IGNORE INTO products (product_id, product_name, price, quantity_in_stock) VALUES 
    (1, 'Laptop', 1200.00, 50),
    (2, 'Smartphone', 800.00, 100),
    (3, 'Headphones', 100.00, 200),
    (4, 'Tablet', 500.00, 75),
    (5, 'Smartwatch', 150.00, 120),
    (6, 'Digital Camera', 300.00, 40),
    (7, 'Bluetooth Speaker', 80.00, 150),
    (8, 'Gaming Console', 400.00, 30),
    (9, 'Wireless Mouse', 25.00, 180),
    (10, 'External Hard Drive', 120.00, 90),
    (11, 'Fitness Tracker', 70.00, 100),
    (12, 'LED Monitor', 200.00, 60),
    (13, 'Portable Printer', 90.00, 25),
    (14, 'USB Flash Drive', 15.00, 250),
    (15, 'Wireless Keyboard', 40.00, 120),
    (16, 'Computer Speakers', 60.00, 80),
    (17, 'Power Bank', 30.00, 150),
    (18, 'Network Router', 50.00, 45),
    (19, 'Graphic Drawing Tablet', 180.00, 35),
    (20, 'Desk Chair', 120.00, 15);
    
 SELECT * FROM products;

-- SELECT * 
-- FROM products 
-- WHERE price > 100;

-- UPDATE products
-- SET quantity_in_stock = quantity_in_stock - 10
-- WHERE product_id > 15;

DELETE FROM products WHERE price > 100;

	
    