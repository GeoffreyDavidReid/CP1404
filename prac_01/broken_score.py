"""
CP1404/CP5632 - Practical
Program to determine score status
"""

score = float(input("Enter score: "))
if score > 100 or score < 0:
    print("Invalid score")
elif score > 90 <= 100:
    print("Excellent")
elif score >= 50 < 90:
    print("Passable")
else:
    print("Bad")