# 3. **Decorators in Practice**: Write a Python program that uses decorators for logging function metadata.
import datetime
import inspect

def logging_function_metadata(func):
    def wrapper_function(*args, **kwargs):

        # print function name
        function_name = func.__name__
        print(f"Function name: {function_name}")

        # print function arguments
        signature = inspect.signature(func)
        print(f"Arguments: {signature}")

        # print time function was called
        current_datetime = datetime.datetime.now()
        print(f"{function_name} was called at: {current_datetime}")
        function_call = func(*args, **kwargs)

        return function_call
    return wrapper_function

@logging_function_metadata
def example_function(a, b, c):
    a = 5
    b = 5
    c = 5
    print(f"a: {a}")


@logging_function_metadata
def read_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
        print(f"Read content from {filename}: {content}")
    return content

example_function(1, 1, 1)
read_file("wek.txt")