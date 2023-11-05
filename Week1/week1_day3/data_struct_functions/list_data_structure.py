# List Manipulation Functions:

# Write functions to perform the following operations on the list:
# Append an element to the end of the list.
# Remove an element from the list.
# Find and return the index of a specific element in the list.
# Sort the list in ascending and descending order.
# Find the maximum and minimum values in the list.

# list manipulation
def list_functions():
    int_list = [2, 1, 3, 6, 5]
    avail_operations = {
        "1": "Append an element to the end of the list.",
        "2": "Remove an element from the list.",
        "3": "Find and return the index of a specific element in the list.",
        "4": "Sort the list in ascending and descending order.",
        "5": "Find the maximum and minimum values in the list.",
    }

    while True:
        print(f"This is the current list: {int_list}\n")
        print(f"Here are the available operations that are available to perform on the list:")
        for key, value in avail_operations.items():
            print(f"{key} - {value}") 
        list_function_operation = int(input("\nPlease select the number of the operation you wish to perform: "))
    
        match list_function_operation:
            case 1:
                int_list = append_element(int_list)
                # append_value = int(input("Provide the integer value you would like to add: "))
                # int_list = int_list.append(append_value)
                # print("Here is your updated list: ", int_list)
            case 2:
                int_list = remove_element(int_list)
            case 3:
                find_return_index(int_list)  
            case 4:
                int_list = sort_list(int_list)  
            case 5:
                find_min_max(int_list)  
            case _:
                print("This is not a valid number for an operation. Please try again.")
                continue
        
        continue_manipulation = str(input("Would you like to continue manipulating the list? (y/n): "))
        if continue_manipulation == "y":
            continue
        elif continue_manipulation == "n":
            break
        else:
            print("This is not a valid response. The list manipulation will now stop.")
            break      
    pass

# append element to list
def append_element(append_list):
    append_value = int(input("Provide the integer value you would like to add: "))
    append_list.append(append_value) 
    print("Here is the new list: ", append_list)
    return append_list


# remove element from list
def remove_element(remove_list):
    remove_value = int(input("Provide the integer value you would like to remove: "))
    remove_list.remove(remove_value)
    print("Here is the new list: ", remove_list)
    return remove_list


# find element at inputted index from list
def find_return_index(index_list):
    index = int(input("What index of the list would you like? "))
    if index not in range(len(index_list)):
        print("Not a valid index!")
    else:
        print(index_list[index])
    return index_list


# sort list ascending or descending
def sort_list(sort_list):
    order =  str(input("Would you like to sort in ascending or descending order? "))
    if order == "ascending":
        sort_list.sort()
    elif order == "descending":
        new_sort_list = sorted(sort_list,reverse=True)
        sort_list.clear()
        sort_list.extend(new_sort_list)
    else:
        print("Not a valid order!")

    print("Here is the new list: ", sort_list)
    return sort_list    


# find the min or max value in list
def find_min_max(min_max_list):
    min_or_max = str(input("Do you want to find the min or max? "))
    if min_or_max == "min":
        value = min(min_max_list)
        print("The minimum value of this list is ", value)
    elif min_or_max == "max":
        value = max(min_max_list)
        print("The maximum value of the list is ", value)
    else:
        print("Not a valid input!")
        value = 0

    return value