"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

keep_looping = True
word_format = ""

def is_valid_format(word_format):
    for kind in word_format:
        if kind == "c" or kind == "v":
            return True
        else:
            return False


word_format = input("Enter word format: ")

while is_valid_format(word_format) == False:
    word_format = input("Enter word format: ")

word = ""
for kind in word_format:
    if kind == "c":
        word += random.choice(CONSONANTS)
    else:
        word += random.choice(VOWELS)

print(word)
