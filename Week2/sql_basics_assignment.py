# Requirements:

# Database Table: Create a table named products with the following columns:
# product_id (integer, primary key)
# product_name (text)
# price (decimal)
# quantity_in_stock (integer)

# Insert Data: Insert at least three rows of data into the products table.

# Data Manipulation: Write SQL queries to perform the following operations:
# Select all products.
# Select products with a price greater than a specified value.
# Update the quantity in stock of a product.
# Delete a product.

# Python Integration: Use the mysql-connector library in Python to connect to the MySQL database, execute SQL queries, and display results.

# import the connect method
import mysql.connector
from mysql.connector import Error

# connector values
host = "localhost"
user = "root"
pw = "37952nsmyahooD!"
db = "sql_queries_week2"

try:
    # establish connection
    connection = mysql.connector.connect(
        host=host, 
        user=user, 
        password=pw, 
        database=db
    )
    print("Connection established")

    # create cursor object
    cursor = connection.cursor()
    print("Cursor object created")

    # select query
    query = "SELECT * FROM products"
    cursor.execute(query)

    result = cursor.fetchall()

    for x in result:
        print(x)

    # close connection
    if connection.is_connected():
        connection.close()
        print("Connection closed.")

except Error as err:
    print('Error message: ' + err.msg)