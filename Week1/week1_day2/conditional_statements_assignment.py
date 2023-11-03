# Ask the user to input their age using input() and convert it to an integer using int().
# Use if, elif (short for "else if"), and else to evaluate different conditions based on the age.
# The program checks if the age is negative, less than 18, less than 65, or equal to or greater than 65, and provides an appropriate message for each condition.

age = int(input("Input your age: "))
if age < 0:
    print("That is an invalid age! Age cannot be negative.")
elif age < 18:
    print("You are a minor.")
elif age < 65:
    print("You can't retire just yet.")
else:
    print("Okay, now you can retire.")