# Custom Modules: Create a Python module that contains functions for basic arithmetic operations. Import this module in another program and use the functions.

# Import add, subtract, multiply, and divide functions from the basic_functions_assignment module

import sys
# print(sys.path)
# sys.path.append("C:\\Users\\Aurora Luong\\Documents\\DataScienceCourse\\Week1\\week1_day2")
# print(sys.path)
from Week1.week1_day2.basic_functions_assignment import add, subtract, multiply, divide

x = add(2, 4)
print(x)

