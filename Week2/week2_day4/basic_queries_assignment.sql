
-- Create a table of employees with employee_id as the primary key 
CREATE TABLE employees (
	employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    job_title VARCHAR(100),
    salary DECIMAL(10,2)
);

-- Insert data into the created table
INSERT INTO employees (
	employee_id, 
    first_name, 
    last_name, 
    job_title, 
    salary
) VALUES (
	1, 
    'John', 
    'Doe', 
    'Software Engineer', 
    75000.00
), (
	2, 
    'Jane', 
    'Smith', 
    'Data Analyst', 
    60000.00
), (
	3, 
    'Bob', 
    'Johnson', 
    'Project Manager', 
    85000.00
);

-- Retrieving Data
-- SELECT * FROM employees;
SELECT employee_id, first_name, last_name FROM employees;