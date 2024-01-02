# 2. **Generators**: Write a Python generator function that yields the Fibonacci sequence.

def fibonacci_generator(limit):
    a,b = 0,1
    while a < limit:
        yield a
        a,b = b,a+b


fib_gen = fibonacci_generator(10)
for i in fib_gen:
    print(i)
        