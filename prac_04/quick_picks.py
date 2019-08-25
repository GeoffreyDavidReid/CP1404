"""
Quick pick program
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
Maximum = 45

def main():
    """Quick picks program - choose sets of random numbers."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("That makes no sense!")
        number_of_quick_picks = int(input("How many quick picks? "))
