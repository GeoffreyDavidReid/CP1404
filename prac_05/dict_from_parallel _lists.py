""" Dictionary from parallel lists function"""

first_list = ("a", "b", "c", "d")
second_list = (1, 2, 3, 4)

def dict_from_lists(first_list, second_list):
    for index in first_list:
        print(index, end=" ")

    print("\n")
    
    for index in second_list:
        print(index, end=" ")

dict_from_lists(first_list, second_list)
