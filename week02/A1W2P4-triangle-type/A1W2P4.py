# A1W2P4 - Triangle type

# Inputs
# side_a = input("Please specify the length of side A:")
# side_b = input("Please specify the length of side B:")
# side_c = input("Please specify the length of side C:")

# a=1, b=2, c=3
raw_input = input("")
side_a = raw_input[2]
side_b = raw_input[7]
side_c = raw_input[12]

# Processing
# Wanneer allemaal ongelijk
# Wanneer 2 gelijk isosceles
# Wanneer abc gelijk equilateral
if side_a == side_b == side_c:
    type = "equilateral"
elif side_a == side_b or side_b == side_c or side_a == side_c:
    type = "isosceles"
else:
    type = "scalene"

# Outputs
print(f"{type}")
