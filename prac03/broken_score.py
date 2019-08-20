"""
CP1404/CP5632 - Practical
Program to determine grade from score
"""

def decide_score(score):
    # function to decide grade from score
    if score > 100 or score < 0:
        return "Invalid score"
    elif score > 90 <= 100:
        return "Excellent"
    elif score >= 50 < 90:
        return "Passable"
    else:
        return "Bad"

score = float(input("Enter score: "))
print("Grade: ", decide_score(score))