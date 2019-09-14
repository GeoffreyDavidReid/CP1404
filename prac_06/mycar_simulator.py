"""
CP1404/CP5632 Practical
Car Driving Simulator
"""

from car import Car

# MENU

def main():
    """main program
    """
    print("Let's go")
    name = input("Enter your car name: ")
    car = Car(name, 100)

