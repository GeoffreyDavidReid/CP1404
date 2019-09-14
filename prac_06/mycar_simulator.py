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
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            distance_to_drive = int(input("How many km do you want to drive? "))
            while distance_to_drive < 0:
                print("Distance must be greater than zero !")
                distance_to_drive = int(input("How many km do you want to drive? "))
            distance_driven = car.drive(distance_to_drive)
            print("The car drove {} km".format(distance_driven))


    distance_to_drive = 100
    distance_driven = car.drive(distance_to_drive)
    print("TEST Distance driven", distance_driven)
    print("TEST ", car)
    fuel_to_add = 200
    car.add_fuel(fuel_to_add)
    print("TEST ", car)

main()

