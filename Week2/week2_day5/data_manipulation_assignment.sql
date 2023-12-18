SELECT * FROM newdb1.employees;

-- Update Records
-- increase salary by 10% for employee with ID=2
UPDATE employees
SET salary = salary * 1.10
WHERE employee_id = 2;

-- Delete Records
-- delete employee with ID = 3
DELETE FROM employees
WHERE employee_id = 3;