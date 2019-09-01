""" Birth dates"""

name_DOB_dict = {}

current_year = 2019
index = 2
for i in range(index):
    name = input("Name: ")
    date_of_birth = input("Date of birth dd/mm/yyy: ")
    day, month, year = date_of_birth.split("/")
    age = current_year - int(year)
    name_DOB_dict[date_of_birth] = name, age
    print("Name: ", name ,"Date of Birth: ", date_of_birth , "Age: ", age)

print("Name DOB Dictionary: ", name_DOB_dict)


