"""
My taxi simulator - based on solution

"""
from car import Car
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

menu = "q)uit, c)hoose, taxi d)rive"


def main():
    """Write a taxi simulator program that uses your Taxi and SilverServiceTaxi
       classes. Each time, until they quit:
       The user should be presented with a list of available taxis and get to
       choose one. Then they should say how far they want to drive.
       At the end of each trip, show them the price and add it to their bill.
        """
