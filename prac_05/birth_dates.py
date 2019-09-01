""" Birth dates"""

name_DOB_dict = {}

index = 2
for i in range(index):
    i = i + 1
    name = input("Name: ")
    date_of_birth = input("Date of birth dd/mm/yyy: ")
    name_DOB_dict[date_of_birth] = name

print("Name DOB Dictionary: ", name_DOB_dict)
