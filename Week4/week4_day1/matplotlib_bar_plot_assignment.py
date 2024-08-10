# 2. **Bar Plot**: Create a Matplotlib bar plot to visualize the grades of a class.

import csv
import matplotlib.pyplot as plt 
import numpy as np 
from collections import Counter

with open('class_grades.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    # read the next line only to check data read
    # print(row['Student'])
    # students = [str(row['Student']) for row in csv_reader]
    # math_grades = [int(row['Math']) for row in csv_reader]
    # # print(math_grades)
    # science_grades = [int(row['Science']) for row in csv_reader]
    # english_grades = [int(row['English']) for row in csv_reader]
    
    math_grade_counter = Counter()
    science_grade_counter = Counter()
    english_grade_counter = Counter()

    for row in csv_reader:
        math_grade_counter.update(row['Math'].split(','))
        science_grade_counter.update(row['Science'].split(','))
        english_grade_counter.update(row['English'].split(','))

math_grade_x = list(math_grade_counter.keys())
num_students_math = list(math_grade_counter.values())

science_grade_x = list(science_grade_counter.keys())
num_students_science = list(science_grade_counter.values())

english_grade_x = list(english_grade_counter.keys())
num_students_english = list(english_grade_counter.values())


# all_grades = math_grade_x + science_grade_x + english_grade_x

# x_indexes = np.arange(len(all_grades))
# # print(x_indexes)
# width = 0.25

# # # count number of students receiving each grade for each subject

# # plt.bar(grades, num_students)
# plt.bar(x_indexes, num_students_math, color="Red", label="Math")
# # plt.bar(x_indexes, num_students_science, color="Green", label="Science")
# # plt.bar(x_indexes + width, num_students_english, color="Yellow", label="English")

# plt.legend()

# plt.title("Grades of the class by subject")
# plt.xlabel("Grade")
# plt.ylabel("Number of students")

# plt.show()