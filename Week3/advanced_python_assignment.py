
import time

# 1. Lambda Functions
# Define a lambda function that takes two parameters and returns their product.
product = lambda a, b: a * b

# Test the lambda function with different values
print("Lambda function result:", product(3,5))

# 2. List Comprehensions
# Generate a list of cubes of even numbers from 1 to 10 using list comprehension.
# append number to new list if even using filter
new_list = list(filter(lambda x: x%2 == 0, list(range(1,11))))
print(new_list)

# Print the list of cubes
print(list(x**3 for x in new_list))

# 3. Decorators
# Create a decorator function that measures the execution time of the decorated function.
def measure_time(func):
    def wrapper(*args, **kwargs):
        # record start time
        start_time = time.time()

        # call original function
        result = func(*args, **kwargs)

        # record end time
        end_time = time.time()

        # execution time
        execution_time = end_time - start_time
        print(f"Execution time: {execution_time} seconds")

        return result
    return wrapper

# Apply the decorator to a sample function
@measure_time
def sample_function(a,b):
    print(product(a,b))

# Test the decorated function with different inputs
sample_function(2,4)
sample_function(3,6)

# 4. Generators
# Create a generator function that yields the squares of numbers up to a specified limit.
def squares_generator(limit):
    a = 1
    while a <= limit:
        yield a*a
        a += 1

# Use the generator to print squares of numbers up to 8
print(list(squares_generator(8)))