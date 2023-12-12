-- basic_queries_assignment for topic: books

-- Create table
CREATE TABLE books (
	book_id INT PRIMARY KEY,
    title VARCHAR(100),
    author VARCHAR(50),
    publication_year INT,
    genre VARCHAR(50)
);

-- Insert data
INSERT INTO books (
	book_id,
    title,
    author,
    publication_year,
    genre
) VALUES (
	1,
    'The Catcher in the Rye',
    'J.D. Salinger',
    1951,
    'Fiction'
), (
	2,
    'To Kill a Mockingbird',
    'Harper Lee',
    1960,
    'Classic'
), (
	3,
    '1984',
    'George Orwell',
    1949,
    'Dystopian'
), (
	4,
    'The Great Gatsby',
    'F. Scott Fitzgerald', 
    1925,
    'Classic'
), (
	5,
    'Harry Potter and the Sorcerer''s Stone',
    'J.K. Rowling',
    1997,
    'Fantasy'
);

-- Retrieve data
SELECT * FROM books;