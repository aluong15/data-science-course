# Loops: Write Python programs that print the first 10 natural numbers using both for and while loops.
# While Loops

# Requirements for the "First 10 Natural Numbers" Program:
# Using a While Loop:

# Create a Python program that prints the first 10 natural numbers.
# Use a while loop to iterate and generate the natural numbers.
# The program should start from 1 and end at 10, inclusively.
# Each natural number should be printed on a separate line.
# The program should not use hard-coded values; it should be able to print the first 10 natural numbers for any desired range.

# request input for starting number
# loop to iterate first 10 natural numbers starting at the starting number
# print each number


start_num = int(input("Choose a starting number: "))
if start_num <= 0:
    print("This is not a natural number!")
else:
    x = start_num
    while x < start_num + 10:
        print(x)
        x += 1
