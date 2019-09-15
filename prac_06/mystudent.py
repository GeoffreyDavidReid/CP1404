"""
CP1404/CP5632 Practical
Student class
"""


class Student:
    """Represent a Student object."""

    def __init__(self, name="", id=0):
        """Initialise a Student instance.

        name: string, reference name for student
        id: integer, student ID
        grade: string P ... C ... D ... HD
        """
        self.name = name
        self.id = id
        self.grade = ""

        def __str__(self):
            """Return a string representation of a Student object."""
        return "{}, ID ={}, grade = {}".format(self.name, self.id,
                                                 self.grade)

    def changeID (self, new_ID):
        """Change student ID."""
        self.id = new_ID

    def changeGrade(self, new_Grade):
        """Change the student grade."""
        self.grade = new_Grade