"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)
    my_car.add_fuel(20) #add this
    my_car.odometer = 10 #add this

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    limo = Car("Limo", 100)
    print(limo.name) # add print
    limo.add_fuel(20)
    print(limo.fuel)
    limo.drive(115)
    print(limo.odometer)

    Chevrolet = Car("Chevrolet", 100) #add new instance
    print(Chevrolet.name) # add print

    #print("TESTCar {}, {}".format(my_car.fuel, my_car.odometer))
    #print("TESTCar {car.fuel}, {car.odometer}".format(car=my_car))


main()
