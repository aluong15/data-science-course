# Tuple Manipulation Functions:

# Write functions to perform the following operations on the tuple:
# Access an element at a specific index.
# Check if a specific element exists in the tuple.
# Count the number of occurrences of a particular element in the tuple.
# Create a new tuple by combining two given tuples.
# Find the length of the tuple.

# tuple manipulation
def tuple_functions():
    str_tuple_1 = ("apple", "banana", "cherry", "cherry", "date")
    str_tuple_2 = ("fig", "grape", "jackfruit")
    avail_operations = {
        "1": "Access an element at a specific index.",
        "2": "Check if a specific element exists in the tuple.",
        "3": "Count the number of occurrences of a particular element in the tuple.",
        "4": "Create a new tuple by combining two given tuples.",
        "5": "Find the length of the tuple.",
    }

    while True:
        print(f"This is the current tuple: {str_tuple_1}\n")
        print(f"Here are the available operations that are available to perform on the tuple:")
        for key, value in avail_operations.items():
            print(f"{key} - {value}") 
        tuple_function_operation = int(input("\nPlease select the number of the operation you wish to perform: "))
    
        match tuple_function_operation:
            case 1: # access element at specific index
                index = int(input("Choose an index: "))
                if index not in range(len(str_tuple_1)):
                    print("Not a valid index!")
                    continue
                else:
                    print(str_tuple_1[index])
            case 2: # check if element exists in tuple
                element = str(input("What element would you like to check for? "))
                if element in str_tuple_1:
                    print(f"Element {element} exists in the tuple!")
                else:
                    print(f"Element {element} does not exist in the tuple!")
            case 3: # count the number of occurrences in tuple
                count = 0
                element = str(input("What element would you like to count for? "))
                for i in range(len(str_tuple_1)):
                    if str_tuple_1[i] == element:
                        count += 1
                print(f"Element {element} occurred {count} times!")
            case 4: # create new tuple by combining two tuples
                new_tuple = str_tuple_1 + str_tuple_2
                print("Here's the new tuple: ", new_tuple)
            case 5: # find length of tuple
                print("The length of the tuple is", len(str_tuple_1))
            case _:
                print("This is not a valid number for an operation. Please try again.")
                continue
        
        continue_manipulation = str(input("Would you like to continue manipulating the tuple? (y/n): "))
        if continue_manipulation == "y":
            continue
        elif continue_manipulation == "n":
            break
        else:
            print("This is not a valid response. The tuple manipulation will now stop.")
            break
