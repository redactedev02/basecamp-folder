# A1W3P6 - Binary to Decimal
# Description: see README.md in this folder

# Inputs binary input as string
binary = input("Input a binary number: ")
total = 0

# processing
for calculation_position in range(len(binary)):
    digit = int(binary[calculation_position])
    power = len(binary) - calculation_position - 1
    total += digit * 2**power

# Outputs
print(total)
