# A1W3P4 - Celsius to Fahrenheit
# Description: see README.md in this folder

# Inputs
# Geen

# Processing
# Code spreekt voor zich
celcius = 10
print("°C °F")
for repeats in range(10):
    fahrenheit = int(celcius * 1.8 + 32)
    print(f"{celcius} {fahrenheit}")
    celcius += 10
