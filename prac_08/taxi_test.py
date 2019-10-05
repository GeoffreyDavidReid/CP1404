""" Test Taxi Class"""

from taxi import Taxi

def main():

    name = input("Name: ")
    fuel = int(input("Fuel: "))
    price_per_km = int(input("Price per km: "))

    taxi1 = Taxi(name, fuel, price_per_km)
    taxi1.drive(20)
    print("TEST2", taxi1)

main()