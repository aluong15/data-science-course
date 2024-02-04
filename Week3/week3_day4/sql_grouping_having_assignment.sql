-- 2. **SQL Grouping**: Write SQL queries that group data using the `GROUP BY` clause 
-- Basic Grouping:
-- Write a query to group the sales data by product_name and calculate the total quantity sold for each product.
SELECT product_name, SUM(quantity_sold) as total_quantity_sold
FROM sales
GROUP BY product_name;

-- Aggregated Values:
-- Extend the basic grouping query to also calculate the sum of the quantity_sold and average unit_price for each product.
SELECT 
	product_name, 
    SUM(quantity_sold) as total_quantity_sold,
    SUM(unit_price) as total_sales_amt,
    AVG(unit_price) as avg_unit_price
FROM sales
GROUP BY product_name;

-- Filtering Grouped Data:
-- Write a query to group the data by products and include only those products where the total quantity sold is greater than 100.
SELECT
	product_name,
    SUM(quantity_sold) as total_quantity_sold
FROM sales
GROUP BY product_name
HAVING total_quantity_sold > 100;

-- Sorting Grouped Data:
-- Modify one of the grouping queries to order the results by the total quantity sold in descending order.
SELECT 
	product_name, 
    SUM(quantity_sold) as total_quantity_sold
FROM sales
GROUP BY product_name
ORDER BY total_quantity_sold DESC;

-- Multiple Grouping Columns:
-- Write a query that groups the sales data by both product_id and product_name to see if there are any duplicate product names.
SELECT
	product_id,
    product_name
FROM sales
GROUP BY product_id, product_name;

-- Grouping with Conditions:
-- Group the data to show the total quantity sold separately for products with a unit price greater than $15 and those with a unit price less than or equal to $15.
SELECT 
	CASE
		WHEN unit_price > 15 THEN "Greater than $15"
        ELSE "Less than or equal to $15"
	END as price_category,
    SUM(quantity_sold) as total_quantity_sold
FROM sales
GROUP by price_category;


-- Nested Grouping:
-- Write a query that includes nested grouping, for example, group by product_category and then by product_name.
SELECT
	product_category,
    product_name,
    SUM(quantity_sold) as total_quantity_sold
FROM sales
GROUP BY
	product_category,
    product_name;


-- Handling NULL Values:
-- Consider scenarios where certain columns may have NULL values. Write a query that groups data while handling NULL values in a specific column (if applicable).
SELECT
    COALESCE(product_name, 'Unknown') as product_name, -- COALESCE returns the first non-NULL value in a list
    product_category,
    SUM(quantity_sold) as total_quantity_sold
FROM
    sales
GROUP BY
    COALESCE(product_name, 'Unknown'), product_category;
-- treats all NULL values in product_name column as Unknown


-- Subqueries with Grouping:
-- Experiment with subqueries to achieve grouping based on conditions or calculations derived from other aggregated values.

-- find products with a quantity sold above the average quantity sold for each product category
SELECT
	product_category,
    product_name,
    SUM(quantity_sold) as total_quantity_sold
FROM sales
GROUP BY
	product_category, product_name
HAVING
	SUM(quantity_sold) > (SELECT AVG(quantity_sold) FROM sales);


