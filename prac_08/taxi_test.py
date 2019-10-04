""" Test Car Class"""

from car import Car

name = input("Name: ")
fuel = int(input("Fuel: "))
#odometer = int(input("Odometer: "))

car1 = Car(name, fuel)

taxi = Car(name, fuel)

print(taxi)