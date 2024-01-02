# 3. **Lambda in List Comprehensions**: Write a Python program that uses both lambda functions and list comprehensions.

# natural_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print([(lambda x: x*x)(x) for x in natural_nums])

original_list = [2, 5, 8, 10, 13, 15, 18, 21, 24, 27]
print("Original list: ", original_list)
squared_list = [(lambda x: x*x)(x) for x in original_list]
print(f"Squared Numbers: {squared_list}")
print("Even Squares:", [y for y in squared_list if y % 2 == 0])
# Even Squares: [4, 64, 100, 324, 576]
