
    ---  <details> <summary>Answers</summary>  
    
    1.  B) Data Visualization
    2.  Matplotlib is a low-level library for creating a wide range of static, animated, and interactive visualizations. Seaborn is a high-level interface built on Matplotlib that comes with improved aesthetics and additional plot types.
    3.  B) Box Plot
    4.  `import seaborn as sns
        import matplotlib.pyplot as plt
        import numpy as np
        
        # Create a 3x3 correlation matrix
        corr_matrix = np.array([[1, 0.8, 0.5], [0.8, 1, 0.3], [0.5, 0.3, 1]])
        
        # Create a heatmap
        sns.heatmap(corr_matrix, annot=True)
        plt.show()`
        
    5.  B) Aesthetics
    6.  `show`
    7.  Key components include data sources, visual elements like charts and graphs, interactivity, and layout design.
    8.  C) A reusable SQL script
    9.  An SQL trigger is a stored procedure that automatically executes in response to certain events on a particular table or view.
    10.  B) Query Optimization
    11.  False
    12.  The `EXPLAIN` keyword is used to obtain a query execution plan, which helps in understanding and optimizing queries.
    13.  A) `CREATE PROCEDURE`
    14.  D) None of the above (Triggers are automatically invoked)
    15.  `CREATE INDEX`
    16.  `CREATE PROCEDURE CalculateAverageSalary()
        BEGIN
         SELECT AVG(Salary) FROM Employees;
        END;`
        
    17.  SQL stored procedures can be called and executed in a Python program using database connectors like `pyodbc` or ORM libraries like `SQLAlchemy`.
        
    
    </details>
