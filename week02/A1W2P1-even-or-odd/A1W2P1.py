# A1W2P1 - Even or Odd
# Description: see README.md in this folder
# Deadline: 2027-01-08 23:59 (CET)

# Inputs
# X een geheel getal (number)
getal = int(input("Number: "))

# Processing
# de rest van getal gedeeld door 2
# even is rest 0
is_even = getal % 2 == 0

# Outputs
# X "Even" als de rest 0 is, anders "Odd"
if is_even:
    print("Even")
else:
    print("Odd")
