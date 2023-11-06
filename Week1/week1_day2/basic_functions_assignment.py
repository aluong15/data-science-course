# Basic Functions: Write Python functions that perform simple arithmetic operations (addition, subtraction, multiplication, division).


def add(a,b):
    """
    Add two numbers and return the result.

    Parameters:
    a (int, float)
    b (int, float)
    """
    return a + b

def subtract(a,b):
    """
    Subtract the second number from the first number and return the result.
    
    Parameters:
    a (int, float)
    b (int, float)
    """
    return a - b

def multiply(a,b):
    """
    Multiply two numbers and return the result.

    Parameters:
    a (int, float)
    b (int, float)
    """
    return a * b

def divide(a,b):
    """
    Divide the first number by the second number and return the result.

    Parameters:
    a (int, float)
    b (int, float), must be nonzero
    """

    if (b == 0):
        return "Error: Division by zero"

    return a / b

 # request user input for numbers and arithmetic operation requested
if __name__ == "__main__":
    a = int(input("a: "))
    b = int(input("b: "))
    arithOperation = input("Arithmetic operation (addition, subtraction, multiplication, division): ")

    # print(type(a))

    #  # check that input parameters are of the expected data type
    # if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
    #     print("Error: Input values must be numbers")

    # if input parameters are valid, perform the arithmetic operation requested and return the result
    if arithOperation == "addition":
        print(add(a,b))
    elif arithOperation == "subtraction":
        print(subtract(a,b))
    elif arithOperation == "multiplication":
        print(multiply(a,b))
    elif arithOperation == "division":
        print(divide(a,b))
    else:
        print("Invalid operation!")


