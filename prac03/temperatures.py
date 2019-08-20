"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""

def celsius_to_fahrenheit(celcius):
    #convert celcius to fahrenheit
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print("Result: {:.2f} F".format(fahrenheit))
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    #convert fahrenheit to celsius
    celsius = 5 / 9 * (fahrenheit - 32)
    print("Result: {:.2f} C".format(celsius))
    return celsius

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        #fahrenheit = celsius * 9.0 / 5 + 32
        #print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        celsius = fahrenheit_to_celsius(fahrenheit)
        #celsius = 5 / 9 * (fahrenheit - 32)
        #print("Result: {:.2f} C".format(celsius))
    else:
        print("Invalid option")
        break
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
