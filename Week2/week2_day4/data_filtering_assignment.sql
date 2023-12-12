-- Data filtering queries on the books table

-- Filtering by a specific condition
-- SELECT * FROM books WHERE publication_year > 1950;

-- Combining conditions
-- SELECT * FROM books WHERE publication_year > 1950 AND genre = 'Classic';

-- Filtering with string patterns
-- SELECT * FROM books WHERE author LIKE 'J%';

-- Filtering with NULL values
-- SELECT * FROM books WHERE author IS NULL;

-- Sorting data
-- SELECT * FROM books WHERE publication_year > 1950 ORDER BY publication_year;

-- Limiting results
SELECT * FROM books WHERE publication_year > 1950 LIMIT 2;