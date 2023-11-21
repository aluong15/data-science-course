# **Basic Exception Handling**: Write a Python program that demonstrates basic exception handling with `try` and `except`.

# User Input:
# Prompt the user to enter a numeric value.
# Ensure that the program can handle both integer and floating-point input.

# Exception Handling:
# Use a try block to attempt to convert the user input to a numeric value.
# Implement an except block to catch and handle any exceptions that may occur during the conversion process.
# Display a user-friendly error message if the input cannot be converted to a numeric value.

# Output:

# If the user input is successfully converted, print a message displaying the converted numeric value.
# If an exception occurs during the conversion, print an error message explaining the issue.

# Repetition:
# Allow the user to make multiple attempts to enter a valid numeric value.
# Implement a loop to repeatedly prompt the user until a valid input is provided.

while True:
    try:
        numeric = float(input("Enter a numeric value: "))
        break
    except ValueError:
        print("Not a numeric value, try again.")

print("User entered a numeric value of ", numeric)