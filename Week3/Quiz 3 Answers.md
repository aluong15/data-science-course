 1   ---  <details> <summary>Answers</summary>  
    
    1.  B) An anonymous function
    2.  List comprehensions provide a concise way to create lists and offer syntactic advantages over using loops.
    3.  A) To modify the behavior of functions
    4.  `def log_metadata(func):
            def wrapper(*args, **kwargs):
                print(f"Function name: {func.__name__}")
                print(f"Arguments: {args}")
                print(f"Keyword arguments: {kwargs}")
                return func(*args, **kwargs)
            return wrapper`
        
    5.  B) A function that yields values one at a time
    6.  `yield`
    7.  Generators are more memory-efficient and often faster for large data sets because they generate values on the fly and do not store them in memory.
    8.  A) `INNER JOIN`
    9.  A subquery is used to retrieve data that will be used in the main query as a condition to further filter the data.
    10.  C) `AVG`
    11.  False
    12.  The `GROUP BY` clause is used to group rows that have the same values in specified columns into summary rows.
    13.  B) `HAVING`
    14.  B) `ORDER BY`
    15.  `COUNT`
    16.  `SELECT Department, AVG(Score) FROM Students GROUP BY Department`
    17.  You can use SQLAlchemy's query API to construct complex SQL queries and execute them using the `session.execute()` method. This allows you to map the results directly to Python objects.
        
    
    </details>
