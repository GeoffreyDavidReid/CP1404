#
# Password Checker
#

def main():

    minimum_length = 10
    password = input("Enter password: ")
    password_ok = True
    while password_ok == True:
        if len(password) > minimum_length:
            break
        password = input("Enter password: ")
    print("Password is: ", password)
    print("Password length: ", len(password))

    for char in password:
        print("*")

main()