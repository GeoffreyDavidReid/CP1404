"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter a valid integer."))
        print(result)
        pass
    except:
        print()
        print("Not a valid integer !!")
print("Valid result is:", result)
