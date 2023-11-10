## Week 6: Software Engineering Best Practices and Data Wrangling - Quiz

### Modular Programming in Python

1. **What is a Python module?**
    - A. A collection of Python classes
    - B. A single Python file that contains functions and variables
    - C. A Python package
    - D. A built-in Python function

2. **Which of the following is the correct way to import a function `my_function` from a module named `my_module`?**
    - A. `import my_function from my_module`
    - B. `from my_module import my_function`
    - C. `import my_module.my_function`
    - D. `import my_module import my_function`

3. **What is the output of the following code if saved in a file named `mymodule.py`?**

    ```python
    def greet(name):
        return f"Hello, {name}"
    
    print(greet("John"))
    ```
    - A. The code will not execute
    - B. The code will print "Hello, John" when `mymodule.py` is imported
    - C. The code will print "Hello, John" when `mymodule.py` is run directly
    - D. Both B and C

### Code Quality and Standards

4. **What is PEP 8?**
    - A. A Python Exception Protocol
    - B. A Python Enhancement Proposal for coding style
    - C. A Python Error Page
    - D. A Python Environment Package

5. **Which Python tool automatically formats code to comply with PEP 8?**
    - A. pylint
    - B. autopep8
    - C. black
    - D. Both B and C

6. **What does a linter do?**
    - A. Formats code
    - B. Checks code for errors and violations of coding standards
    - C. Compiles code
    - D. Executes code

### Data Wrangling with Pandas

7. **Which Pandas function is used to reshape data from wide to long format?**
    - A. `pivot`
    - B. `melt`
    - C. `reshape`
    - D. `stack`

8. **What does the `agg` function in Pandas do?**
    - A. Aggregates data using one or more operations over the specified axis
    - B. Aggregates data using only a single operation over the specified axis
    - C. Adds a new column to the DataFrame
    - D. None of the above

### Version Control Best Practices

9. **What is the primary purpose of branching in Git?**
    - A. To delete the main branch
    - B. To create a copy of your codebase for isolated development
    - C. To merge changes into the main branch
    - D. To clone a repository

10. **What is a Pull Request in GitHub?**
    - A. A request to pull changes from one branch to another
    - B. A request to delete a branch
    - C. A request to clone a repository
    - D. A request to push changes to a branch

### Integration and Testing

11. **What is the primary purpose of unit testing?**
    - A. To test individual components of the software in isolation
    - B. To test the interaction between different components of the software
    - C. To test the software on different operating systems
    - D. To test the user interface of the software

12. **Which Python library is commonly used for writing unit tests?**
    - A. unittest
    - B. pytest
    - C. doctest
    - D. All of the above

### Week 6 Checkpoint

13. **What is the primary advantage of modular programming?**
    - A. Faster execution time
    - B. Easier debugging and maintenance
    - C. Reduced memory usage
    - D. All of the above

14. **What is integration testing primarily concerned with?**
    - A. Testing individual components in isolation
    - B. Testing the interaction between different components
    - C. Testing the user interface
    - D. Testing database connections

15. **In a Git workflow, what does `git merge` do?**
    - A. Creates a new branch
    - B. Deletes a branch
    - C. Combines changes from different branches
    - D. Clones a repository

16. **Which of the following code snippets correctly normalizes a column named 'Age' in a Pandas DataFrame `df`?**
    ```python
    A. df['Normalized_Age'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())
    B. df['Normalized_Age'] = df['Age'] / df['Age'].max()
    C. df['Normalized_Age'] = df['Age'] - df['Age'].mean()
    D. df['Normalized_Age'] = (df['Age'] - df['Age'].mean()) / df['Age'].std()
    ```
