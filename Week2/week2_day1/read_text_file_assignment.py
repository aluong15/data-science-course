# **Read Text File**: Write a Python program that reads a text file and prints its content.

with open('test.txt', 'r') as f:

    for line in f:
        print(line, end='')

