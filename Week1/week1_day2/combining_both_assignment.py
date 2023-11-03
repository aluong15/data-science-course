# Combining Both: Write a Python function that takes an integer as input and prints whether the number is even or odd.

# Clearer requirements:
# The function should be named check_even_or_odd.
# It should take one argument, an integer num, which represents the number to be checked.
# The function should print whether the number is even or odd using a clear message.
# It should use a conditional statement (if-else) to determine if the input integer is even or odd.
# If the input number is even, the function should print "The number [num] is even."
# If the input number is odd, the function should print "The number [num] is odd."
# The function should not return any value; it should only print the result.

def check_even_or_odd(num):
    """
    Prints out whether the number num is even or odd
    
    Parameters:
    num (int)
    """
    if num == 0:
        print("This number is not even nor odd!")
    elif num % 2 == 0:
        print(f"This number {num} is even.")
    elif num % 2 == 1:
        print(f"This number {num} is odd.")
    else:
        print(f"This isn't a number?")
    
num = int(input("Enter a number: "))
check_even_or_odd(num)
