# file practice programs
#
# 1. prompt user for their name
# 2. open a file name.txt
# 3. print "Your name is XXX"

name = input("Enter name")
out_file = open("name.txt", 'w')
print(name, file=out_file)
out_file.close()

in_file = open("numbers.txt", 'r')
number1 = in_file.readline().strip()
number1_int = int(number1)
print("Number1 = ", number1)
number2 = in_file.readline().strip()
number2_int = int(number2)
print("Number2 = ", number2)

result = number1_int + number2_int

print("Result ", result)

in_file.close()

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print()
print("sum is: ", total)