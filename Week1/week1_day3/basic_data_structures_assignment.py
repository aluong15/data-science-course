# Basic Data Structures: Create a list, tuple, and dictionary with arbitrary elements. Write functions to manipulate these data structures.

# Data Structure Creation:

# Create a list, a tuple, and a dictionary, each containing arbitrary elements. These elements can be of any data type (e.g., integers, strings, floats, etc.).

# User Interaction: Create a user interface that allows the user to choose which data structure they want to manipulate and which operation to perform.
# Documentation: Provide clear and concise documentation for your code, including comments explaining the purpose and functionality of each function.

# from week1_day3.data_struct_functions.list_data_structure import list_functions
# from week1_day3.data_struct_functions.list_data_structure import perform_list_operation
from data_struct_functions.list_data_structure import *
from data_struct_functions.dictonary_data_structure import *
from data_struct_functions.tuple_data_structure import *

# available operations
valid_operations = ["list", "tuple", "dictionary"]

# data structures and available operations for each
def data_struct_operations(selected_data_struct):
    match selected_data_struct:
        case "list":
            list_functions()
        case "tuple":
            tuple_functions()
        case "dictionary":
            dictionary_functions()
        case _:
            print("Not a valid data structure.")

while True:
    # ask user what data structure they want to manipulate
    data_struct_selection = str(input(f"What data structure would you like to manipulate ({valid_operations}): "))

    if data_struct_selection not in valid_operations:
        print("That is not one of the available data structures that can be manipulated here. Try again!")
        continue

    else:
        data_struct_operations(data_struct_selection)
        
    break
