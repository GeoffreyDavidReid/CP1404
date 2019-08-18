"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? ---- numerator and or denominator are not integers
2. When will a ZeroDivisionError occur? ---- denominator = zero
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0: # line added
        denominator = int(input("Enter the denominator: ")) # line added
        if denominator != 0: # line added
            break # line added
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
