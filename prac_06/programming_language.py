"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year, author): #add author
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
        self.author = author # new line added

    def __str__(self):
        """Return string representation of a ProgrammingLanguage."""
        return "{}, {} Typing, Reflection={}, First appeared in {}, Was authored by {}".format(
            self.name, self.typing, self.reflection, self.year, self.author) #added author

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995, "Jack")
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991, "Jill")
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991, "Thomas")

    languages = [ruby, python, visual_basic]
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)
            print("test author: ", language.author) #add line


if __name__ == "__main__":
    run_tests()
