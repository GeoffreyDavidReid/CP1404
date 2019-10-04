""" Test Car Class"""

from car import Car

name = input("Name: ")
fuel = int(input("Fuel: "))
odometer = int(input("Odometer: "))

taxi = Car(name, fuel, odometer)

name = input("Name: ")
fuel = int(input("Fuel: "))
odometer = int(input("Odometer: "))

car1 = Car(name, fuel, odometer)

print(taxi)
print(car1)

taxi.add_fuel(12)

print(taxi)
