# A1W2P3 - Sides to shape
# Description: see README.md in this folder
# Deadline: 2027-01-08 23:59 (CET)

# Inputs
sides = int(input("Sides: "))

# Processing
if sides == 3:
    name = "Triangle"
elif sides == 4:
    name = "Square"
elif sides == 5:
    name = "Pentagon"
elif sides == 6:
    name = "Hexagon"
elif sides == 7:
    name = "Heptagon"
elif sides == 8:
    name = "Octagon"
elif sides == 9:
    name = "Nonagon"
elif sides == 10:
    name = "Decagon"
else:
    name = "Amount of sides is out of range"

# Outputs
print(name)
