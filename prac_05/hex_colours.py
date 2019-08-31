"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

COLOUR_NAMES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb"}
#print(COLOUR_NAMES)

colour_name = input("Enter colour name ie AliceBlue: ")
#colour_name = str.upper(colour_name)
while colour_name != "":
    if colour_name in COLOUR_NAMES:
        print("{} is {}".format(colour_name, COLOUR_NAMES[colour_name]))
    else:
        print("Invalid colour name")
    colour_name = input("Enter colour name ie: AliceBlue ")
    #colour_name = str.upper(colour_name)
print()
for colour_name in COLOUR_NAMES:
    print("{} is {}".format(colour_name, COLOUR_NAMES[colour_name]))