# 1. **Decorators**: Write a Python decorator that measures the execution time of a function.

import time

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

# apply decorator function
@measure_time
def example_function():
    time.sleep(2)

example_function()