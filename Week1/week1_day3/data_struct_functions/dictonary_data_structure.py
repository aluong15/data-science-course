# Dictionary Manipulation Functions:

# Write functions to perform the following operations on the dictionary:
# Add a new key-value pair to the dictionary.
# Remove a key-value pair from the dictionary.
# Retrieve the value associated with a specific key.
# Check if a key exists in the dictionary.
# List all the keys and values in the dictionary.

# dictionary manipulation
def dictionary_functions():
    float_dict = {
        "value1": 3.14,
        "value2": 1.618,
        "value3": 2.718,
        "value4": 0.577,
    }

    avail_operations = {
        "1": "Add a new key-value pair to the dictionary.",
        "2": "Remove a key-value pair from the dictionary.",
        "3": "Retrieve the value associated with a specific key.",
        "4": "Check if a key exists in the dictionary.",
        "5": "List all the keys and values in the dictionary.",
    }

    while True:
        print("This is the current dictionary: \n")
        print_dict(float_dict)
        print(f"\nHere are the available operations that are available to perform on the dictionary:")
        for key, value in avail_operations.items():
            print(f"{key} - {value}") 
        dict_function_operation = int(input("\nPlease select the number of the operation you wish to perform: "))
    
        match dict_function_operation:
            case 1: # add a new key-value pair to the dict
                key_add = str(input("What key would you like to add? "))
                if is_key_in_dict(key_add, float_dict):
                    print(f"The key {key_add} already exists! It will not be added.")
                    continue
                else:
                    value_add = float(input("What corresponding value would you like to add? "))
                    float_dict[key_add] = value_add
                    print("Here is the updated dictionary: ")
                    print_dict(float_dict)

            case 2: # remove a key-value pair from the dict
                key_remove = str(input("What key would you like to remove? "))
                if is_key_in_dict(key_remove, float_dict):
                    del float_dict[key_remove]
                    print("Here is the updated dictionary: ")
                    print_dict(float_dict)
                else:
                    print("This key does not exist!")
                    continue

            case 3: # retrieve the value associated with a specific key
                key_wanted = str(input("What key would you like to see its corresponding value for? "))
                if is_key_in_dict(key_wanted, float_dict):
                    value_wanted = float_dict.get(key_wanted)
                    print(f"The value associated with {key_wanted} is {value_wanted}")
                else:
                    print("This key does not exist!")
                    continue
                    
            case 4: # check if a key exists in the dict
                key_wanted = str(input("What key would you like to check if it exists in the dictionary? "))
                if is_key_in_dict(key_wanted, float_dict):
                    print(f"The key {key_wanted} exists!")
                else:
                    print("This key does not exist!")
                    continue

            case 5: # list all the keys and values in the dictionary
                print("Here are all the keys and values in the dictionary: ")
                print_dict(float_dict)
            case _:
                print("This is not a valid number for an operation. Please try again.")
                continue
        
        continue_manipulation = str(input("\nWould you like to continue manipulating the dictionary? (y/n): "))
        if continue_manipulation == "y":
            continue
        elif continue_manipulation == "n":
            break
        else:
            print("This is not a valid response. The dictionary manipulation will now stop.")
            break

def print_dict(current_dict):
    for key, value in current_dict.items():
        print(f"{key} - {value}") 

def is_key_in_dict(key, current_dict):
    return key in current_dict
