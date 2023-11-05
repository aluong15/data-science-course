# Combining Both: Write a Python function that takes a list of numbers and returns their sum using a loop.

input_list = []

def calculate_sum(input_list):
    sum_list = 0.0
    for i in input_list:
        if isinstance(i, float):
            sum_list += i
    return sum_list

# request values to input in list
while True:
    if not input_list:
        print("The list is empty.")
    else:
        print("The current list is", input_list)

    keep_adding_to_list = str(input("Would you like to add to the list (y/n) "))
    if keep_adding_to_list == "y":
        new_list_value = float(input("Input the float value you want to add to the list: "))
        input_list.append(new_list_value)
    elif keep_adding_to_list == "n":
        print("The final list is", input_list)
        break
    else:
        print("That is not a valid input! Try again.")
        continue

print("The sum of the numbers in the list is: ", calculate_sum(input_list))
