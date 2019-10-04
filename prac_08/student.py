"""
CP1404/CP5632 Practical
Student class
"""


class Student:
    """Represent a Student object."""

    def __init__(self, first_name="", second_name="", student_ID=0):
        """Initialise a Car instance.

        first_name: string, reference first name for student
        last_name: string, reference last first name for student
        student_ID: integer,reference studentID for student
        """
        self.first_name = first_name
        self.second_name = second_name
        self.studentID = student_ID

    def __str__(self):
        """Return a string representation of a Car object."""
        return ("First name: {}, Second name: {}, Student ID: {}".format(self.first_name, self.second_name,
                                                 self.studentID))

    # def add_fuel(self, amount):
    #     """Add amount to the car's fuel."""
    #     self.fuel += amount
    #
    # def drive(self, distance):
    #     """Drive the car a given distance.
    #
    #     Drive given distance if car has enough fuel
    #     or drive until fuel runs out return the distance actually driven.
    #     """
    #     if distance > self.fuel:
    #         distance = self.fuel
    #         self.fuel = 0
    #     else:
    #         self.fuel -= distance
    #     self.odometer += distance
    #     return distance
