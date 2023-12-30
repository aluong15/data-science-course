# import the connect method
import mysql.connector
from mysql.connector import Error

# connector values
host = "localhost"
user = "root"
pw = "37952nsmyahooD!"
db = "sm_app"

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
    query = "SELECT id, name, nationality FROM users"
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