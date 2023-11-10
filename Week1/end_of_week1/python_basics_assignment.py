# **Python Basics**: Write a Python program that uses conditional statements, loops, and data structures to solve a real-world problem of your choice.

# Let's create a Python program that simulates a simple grade calculator. The program will take input for the number of students, their names, and their scores in three subjects. Then, it will calculate the average score for each student and assign a letter grade based on the average.

# Here are the requirements for the program:

# User Input:

# Prompt the user to enter the number of students.
# For each student, ask for their name and scores in three subjects (let's say Math, English, and Science).

# Data Processing:

# Calculate the average score for each student.
# Assign a letter grade based on the average score. Use the following grading scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Output:

# Display the student names, their average scores, and the corresponding letter grades.

# Additional Requirements:

# Use conditional statements to determine the letter grade.
# Implement a loop to handle multiple students.
# Utilize appropriate data structures (lists, dictionaries) to store and process the information.

def calculate_grade(score):
    # Function to calculate the letter grade based on the score
    # Add your logic here
    if score >= 90 and score <= 100:
        return "A"
    elif score >= 80 and score < 90:
        return "B"
    elif score >= 70 and score < 80:
        return "C"
    elif score >= 60 and score < 70:
        return "D"
    else:
        return "F"

# Get the number of students
num_students = int(input("Enter the number of students: "))

# Initialize an empty list to store student information
students = []

# Loop through each student
for i in range(num_students):
    # Get student name
    name = input(f"Enter the name of student {i + 1}: ")

    # Get scores for each subject
    math_score = float(input("Enter Math score: "))
    english_score = float(input("Enter English score: "))
    science_score = float(input("Enter Science score: "))

    # Calculate the average score
    average_score = (math_score + english_score + science_score) / 3

    # Calculate the letter grade using the calculate_grade function
    grade = calculate_grade(average_score)

    # Store the student information in a dictionary
    student_info = {
        "Name": name,
        "Math": math_score,
        "English": english_score,
        "Science": science_score,
        "Average": average_score,
        "Grade": grade,
    }

    # Add the student information to the list
    students.append(student_info)

# Display the results
print("\nStudent Report:")
for student in students:
    print(f"\nName: {student['Name']}")
    print(f"Average Score: {student['Average']}")
    print(f"Grade: {student['Grade']}")
