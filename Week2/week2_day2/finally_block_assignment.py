# **Finally Block**: Write a Python program that uses `finally` to execute code after `try` and `except`.

# User Input:
# Prompt the user to enter two numeric values: one for the numerator and one for the denominator.
# Ensure that the program can handle both integer and floating-point input for both numerator and denominator.

# Exception Handling:
# Use a try block to perform the division operation (numerator divided by denominator).
# Implement an except block to catch and handle any exceptions that may occur during the division.
# Use a finally block to execute code that must run regardless of whether an exception was raised or not.

# Output:
# Display the result of the division if it is successful.
# If an exception occurs, print a user-friendly error message explaining the issue.
# Ensure that the message in the finally block is also displayed.

# Repetition:
# Allow the user to make multiple attempts to enter valid values for numerator and denominator.
# Implement a loop to repeatedly prompt the user until a valid input is provided.

while True:
    try:
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        division = numerator / denominator
        break

    except ValueError:
        print("Not a numeric value, try again.")

    except ZeroDivisionError:
        print("Cannot divide by zero. Try again.")

    finally:
        print("Finally block reached.")

print(f"The division of {numerator} by {denominator} is: {division}")
