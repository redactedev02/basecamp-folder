# A1W2P2 - Leap year
# Description: see README.md in this folder
# Deadline: 2027-01-08 23:59 (CET)

# Inputs
year = int(input("Enter a year: "))

# Processing
if year % 400 == 0:
    leap = True
elif year % 100 == 0:
    leap = False
elif year % 4 == 0:
    leap = True
else:
    leap = False

# Outputs
if leap:
    print("Leap year")
else:
    print("Not a leap year")
