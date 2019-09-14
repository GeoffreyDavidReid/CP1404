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
    print(car)
    #MENU
    #choice = input("Enter your choice: ").lower()
    distance_to_drive = 100
    distance_driven = car.drive(distance_to_drive)
    print("TEST Distance driven", distance_driven)
    print("TEST ", car)


main()

