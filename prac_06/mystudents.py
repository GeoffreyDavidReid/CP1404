""" My student main program
    Test student class.
"""
from mystudent import Student

def main():

    student = Student()
    #print(student)
    student.name = "Geoff"
    student.ID = 123456
    student.grade = "D"
    #print(student)
    new_student_grade = "HD"
    #print("TEST ",new_student_grade)
    student.changeGrade(new_student_grade)
    new_student_ID = 111111
    student.changeID(new_student_ID)
    print(student)

main()
