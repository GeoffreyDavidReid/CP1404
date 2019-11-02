"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06_car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return (s + " ") * (n - 1) + s

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # TODO: 1. fix the repeat_string function above so that it passes the failing test
    # Done

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    # TODO: 2. write assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    #assert test_car.fuel == 0, "Should fail"
    assert test_car.fuel == 10, "Should pass"
    #assert test_car.fuel == 15, "Should fail"


run_tests()

# TODO: 3. Uncomment the following line and run the doctests
# Done
doctest.testmod()

# TODO: 4. Fix the failing is_long_word function
# Done

# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
# 'hello' -> 'Hello.'
# 'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more you decide (one that is valid!)
# test this and watch the tests fail
# then write the body of the function so that the tests pass

def format_a_phrase_as_a_sentence():
    pass
"""
>>> format_a_phrase_as_a_sentence('hello'):
'Hello.'
>>> format_a_phrase_as_a_sentence('It is an ex parrot.')
'It is an ex parrot.'
"""
doctest.testmod()