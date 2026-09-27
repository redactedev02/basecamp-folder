# A1W2P5 - Dutch holidays
# Description: see README.md in this folder
# Deadline: 2026-09-18 23:59 (CEST)

# Inputs
date = input("Date: ")

# Processing
# woorden weghalen, zodat alleen "12, 5" overblijft
schoon = date.replace("Date: ", "").replace("Month: ", "").replace("Day: ", "")
# knippen op de komma: ["12", " 5"]
delen = schoon.split(",")
# van tekst naar getal
month = int(delen[0])
day = int(delen[1])

if month == 1 and day == 1:
    feestdag = "Nieuwjaarsdag"
elif month == 4 and day == 27:
    feestdag = "Koningsdag"
elif month == 5 and day == 5:
    feestdag = "Bevrijdingsdag"
elif month == 12 and day == 5:
    feestdag = "Sinterklaas"
elif month == 12 and (day == 25 or day == 26):
    feestdag = "Kerstmis"
else:
    feestdag = "No holiday found on given input."

# Outputs
print(feestdag)
