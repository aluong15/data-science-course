# make a connection to a MySQL server
# execute a separate query to create the database

# define function that connects to mySQL database server and returns the connection object
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
            
        )
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "root", "37952nsmyahooD!")

# create database function
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

# create database
create_database_query = "CREATE DATABASE sm_app"
create_database(connection, create_database_query)

# execute query function
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

execute_query(connection, "USE sm_app")

create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT,
    name TEXT NOT NULL,
    age INT,
    gender TEXT,
    nationality TEXT,
    PRIMARY KEY (id)
)   ENGINE = InnoDB;
"""
# execute create query
execute_query(connection, create_users_table)

# INSERT
create_users = """
INSERT INTO
    users (name, age, gender, nationality)
VALUES
    ('James', 25, 'male', 'USA'),
    ('Leila', 32, 'female', 'France'),
    ('Brigitte', 35, 'female', 'England'),
    ('Mike', 40, 'male', 'Denmark'),
    ('Elizabeth', 21, 'female', 'Canada');
"""

execute_query(connection, create_users)

# SELECT
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error {e} has occurred")
    finally:
        if cursor:
            cursor.close()

select_users = "SELECT * FROM users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)

# UPDATE
update_user = """
UPDATE users
SET age = age + 2
WHERE id = 2;
"""

execute_query(connection, update_user)
updated_users = execute_read_query(connection, select_users)
print("UPDATE: ")
for user in updated_users:
    print(user)


# DELETE
delete_user = """
DELETE FROM users
WHERE name = 'Elizabeth'
"""

execute_query(connection, delete_user)
deleted_users = execute_read_query(connection, select_users)
print("DELETE UPDATE: ")
for user in deleted_users:
    print(user)


# close database
if connection.is_connected():
    connection.close()
    print("Connection closed.")