"""
CP1404/CP5632 Practical
Car Driving Simulator
"""

from car import Car

MENU = "Menu:\nd) drive\nr) refuel\nq) quit"

def main():
    """main program
    """
    print("Let's go")
    name = input("Enter your car name: ")
    car = Car(name, 100)
    print(car)
    print(MENU)
    choice = input("Enter your choice: ").lower()
    while choice != "q":
        if choice == "d":
            distance_to_drive = int(input("How many km do you want to drive? "))
            while distance_to_drive < 0:
                print("Distance must be greater than zero !")
                distance_to_drive = int(input("How many km do you want to drive? "))
            distance_driven = car.drive(distance_to_drive)
            print("The car drove {} km ".format(distance_driven), end = "")
            if car.fuel == 0:
                print("and ran out of fuel", end="")
                print(".")
        elif choice == "r":
            fuel_to_add = int(input("How many units of fuel do you wish to add ?"))
            while fuel_to_add < 0:
                print("Fuel to add must be >= zero")
                fuel_to_add = int(input("How many units of fuel do you wish to add ?"))
            car.add_fuel(fuel_to_add)
            print("Added {} units of fuel".format(fuel_to_add))
        else:
            print("Invalid choice")
        print()
        print(car)
        print(MENU)
        choice = input("Enter your choice: ").lower()
    print("\nGoodbye {}'s driver".format(car.name))

main()

