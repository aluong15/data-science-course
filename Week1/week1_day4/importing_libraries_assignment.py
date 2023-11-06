# Importing Libraries: Write a Python program that imports a standard library (e.g., math, datetime) and uses at least two of its functionalities.

# Library Choice: Use the datetime library for working with dates and times.

# Import the Library: Import the datetime library at the beginning of your Python script using the import statement:

# Use Two Functionalities:
# a. Calculate the current date and time using the datetime.now() function.
# b. Add a specific number of days to the current date using the timedelta object.

# imported datetime and timedelta functions from the datetime library
from datetime import datetime, timedelta

# get the current datetime
current_datetime = datetime.now()
print("The current datetime is ", current_datetime)

# add a specific number of days to the current date
future_datetime = current_datetime + timedelta(days=3, seconds=7, minutes=14, hours=6)
print("The future datetime in 3 days, 6 hours, 14 minutes, and 7 seconds is: ", future_datetime)