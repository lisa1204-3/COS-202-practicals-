#!/usr/bin/python3

import time
 
t = time.localtime(time.time())
localtime = time.asctime(t)
str = "Current Time:" + time.asctime(t)
 
print(str)# ===========================================
# PERSONAL POCKET CGPA CALCULATOR (PPC)
# ===========================================

print("=" * 50)
print("      PERSONAL POCKET CGPA CALCULATOR")
print("=" * 50)

# Student Details
name = input("Enter Student Name: ")
matric = input("Enter Matric Number: ")
department = input("Enter Department: ")
level = input("Enter Level: ")

num_courses = int(input("\nEnter Number of Courses Offered: "))

total_units = 0
total_grade_points = 0

print("\nCourse Details")
print("-" * 50)

for i in range(num_courses):

    print(f"\nCourse {i+1}")

    course_code = input("Course Code: ")
    course_unit = int(input("Course Unit: "))
    score = int(input("Score (0 - 100): "))

    # Determine Grade
    if score >= 70:
        grade = "A"
        point = 5

    elif score >= 60:
        grade = "B"
        point = 4

    elif score >= 50:
        grade = "C"
        point = 3

    elif score >= 45:
        grade = "D"
        point = 2

    elif score >= 40:
        grade = "E"
        point = 1

    else:
        grade = "F"
        point = 0

    grade_point = point * course_unit

    total_units += course_unit
    total_grade_points += grade_point

    print("Grade:", grade)
    print("Grade Point:", grade_point)

# Calculate GPA
gpa = total_grade_points / total_units

print("\n" + "=" * 50)
print("           STUDENT RESULT")
print("=" * 50)

print("Name          :", name)
print("Matric No.    :", matric)
print("Department    :", department)
print("Level         :", level)
print("Total Units   :", total_units)
print("Total Points  :", total_grade_points)
print("GPA           :", round(gpa, 2))

# Class of Degree
print("\nAcademic Standing")

if gpa >= 4.50:
    print("Class of Degree: FIRST CLASS")

elif gpa >= 3.50:
    print("Class of Degree: SECOND CLASS UPPER")

elif gpa >= 2.40:
    print("Class of Degree: SECOND CLASS LOWER")

elif gpa >= 1.50:
    print("Class of Degree: THIRD CLASS")

elif gpa >= 1.00:
    print("Class of Degree: PASS")

else:
    print("Class of Degree: FAIL")

print("=" * 50)
print("Thank you for using the Personal Pocket")
print("CGPA Calculator.")
print("=" * 50)