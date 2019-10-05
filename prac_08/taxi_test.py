""" Test Taxi Class"""

from taxi import Taxi

def main():

    name = input("Name: ")
    fuel = int(input("Fuel: "))
    price_per_km = float(input("Price per km $: "))

    taxi1 = Taxi(name, fuel, price_per_km)
    taxi1.drive(40)
    print("TEST2", taxi1)
    current_fare = taxi1.get_fare()
    print("TEST3", current_fare)

main()