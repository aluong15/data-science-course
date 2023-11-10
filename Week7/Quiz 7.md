## Week 7: Web Scraping, APIs, and Automation - Quiz

### Multiple Choice Questions

#### Introduction to Web Scraping

1. **Which Python library is commonly used for web scraping?**
    - A. NumPy
    - B. BeautifulSoup
    - C. Selenium
    - D. Pandas

#### Web Scraping with Selenium

2. **What is Selenium primarily used for?**
    - A. Data Analysis
    - B. Web Scraping Static Websites
    - C. Web Scraping Dynamic Websites
    - D. Data Visualization

#### Working with APIs

3. **Which HTTP method is commonly used to fetch data from an API?**
    - A. GET
    - B. POST
    - C. PUT
    - D. DELETE

#### Web Automation

4. **Which of the following tasks can be automated using Selenium?**
    - A. Form Submission
    - B. Clicking Buttons
    - C. Navigating Through Web Pages
    - D. All of the above

#### Scripting and Automation Best Practices

5. **What is the primary purpose of logging in a script?**
    - A. Debugging
    - B. User Authentication
    - C. Data Storage
    - D. Data Encryption

### Short Answer Questions

6. **Explain the difference between web scraping static and dynamic websites.**

7. **What are the key considerations when scraping a website?**

8. **Describe the typical steps involved in making an API request in Python.**

9. **What are some best practices for web automation?**

10. **Why is modular programming important in scripting and automation?**

### Code Snippet Questions

11. **Write a Python code snippet that uses BeautifulSoup to scrape and print all the links (`<a>` tags) from a given HTML.**

12. **Write a Python code snippet that uses Selenium to open a web page and fill out a form with the id `myForm`. Assume the form has fields with ids `username` and `password`.**

13. **Write a Python code snippet to make a GET request to an API endpoint and parse the JSON response to get a specific field named `data`. Use the `requests` library.**

14. **Write a Python code snippet to implement logging in an existing script. Log messages for start, end, and any errors.**

15. **Write a Python code snippet that refactors the following script into a modular format.**

    ```python
    import requests

    def fetch_data():
        response = requests.get('https://api.example.com/data')
        if response.status_code == 200:
            return response.json()
        else:
            return None

    data = fetch_data()
    if data:
        print("Data fetched successfully.")
    else:
        print("Failed to fetch data.")
    ```
