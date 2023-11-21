# **Multiple Exceptions**: Write a Python program that catches different types of exceptions.

# User Input:
# Prompt the user to enter two values: one for the numerator and one for the denominator.
# Ensure that the program can handle both integer and floating-point input for both numerator and denominator.

# Exception Handling:
# Use a try block to perform the division operation (numerator divided by denominator).
# Implement multiple except blocks to catch and handle different types of exceptions that may occur during the division.
# Handle the case where the denominator is zero separately.
# Handle cases where the user enters non-numeric values.

# Output:
# Display the result of the division if it is successful.
# If an exception occurs, print a user-friendly error message explaining the issue.

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

print(f"The division of {numerator} by {denominator} is: {division}")
