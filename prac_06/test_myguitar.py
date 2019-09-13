"""
CP1404/CP5632 Practical - Suggested Solution
Basic manual tests for Guitar class
"""
from myguitar import Guitar # test this code using my guitar class

CURRENT_YEAR = 2019


def run_tests():
    """Tests for Guitar class."""
    name = "Fender"
    year = 1966
    cost = 3600

    guitar = Guitar(name, year, cost)
    other = Guitar("Another guitar", 1954, 5000)

    #print(guitar)

    print("{} get_age() - Expected {}. Got {}".format(guitar.name,53,guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 65, other.get_age()))


if __name__ == '__main__':
    run_tests()