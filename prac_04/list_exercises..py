
# Basic list operations
numbers = []
number_to_process = int(input("Numbers to process: "))
for i in range(number_to_process):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is", numbers[0])
print("The last number is", numbers[-1])
print("The smallest number is", min(numbers))
print("The largest number is", max(numbers))
print("The average of the numbers is", sum(numbers) / len(numbers))

# Security checker...

# Create usernames list
usernames = []
print()
length_of_list = int(input("Length of username list: ")) # Input length of usernames list

for i in range(length_of_list):
    username = input("Username: ")
    usernames.append(username)

print()
username = input("Enter username:")
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
