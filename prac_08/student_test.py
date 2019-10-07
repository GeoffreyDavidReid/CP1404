"""
Testing my Student class
"""
from student import Student

first_name = input("First_name: ")
second_name = input("Second_name: ")
studentID = int(input("StudentID: "))

student1 = Student(first_name, second_name, studentID)

print(student1)