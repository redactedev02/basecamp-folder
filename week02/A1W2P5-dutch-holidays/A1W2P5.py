# A1W2P5 - Dutch holidays
# Description: see README.md in this folder
# Deadline: 2027-01-08 23:59 (CET)

# Inputs: Input is given as a comma separated string: Date: Month: 12, Day: 5
date = "Month: 1, Day: 01"

# Processing, seperating month and day
# opschonen van input
# splitsen van input
# in standaardvorm zetten

schoon = date.replace("Date:", "").replace("Month:", "").replace("Day:", "")
print(schoon)
delen = schoon.split(",")
month = int(delen[0])
day = int(delen[1])
vergelijking = f"{month:02d}{day:02d}"


# Collection feestdagen
# Nieuwjaarsdag: donderdag 1 januari 2026
# Goede Vrijdag: vrijdag 3 april 2026
# Pasen (eerste en tweede paasdag): zondag 5 april en maandag 6 april 2026
# Koningsdag: maandag 27 april 2026
# Bevrijdingsdag: dinsdag 5 mei 2026
# Hemelvaartsdag: donderdag 14 mei 2026
# Pinksteren (eerste en tweede pinksterdag): zondag 24 mei en maandag 25 mei 2026
# Kerstmis: vrijdag 25 december en zaterdag 26 december 2026

if vergelijking == "0101":
    feestdag = "Nieuwjaarsdag"
elif vergelijking == "0403":
    feestdag = "Pasen"
elif vergelijking == "0427":
    feestdag = "Koningsdag"
elif vergelijking == "0505":
    feestdag = "Bevrijdingsdag"
elif vergelijking == "0514":
    feestdag = "Hemelvaart"
elif vergelijking in ("0524", "0525"):
    feestdag = "Pinksteren"
elif vergelijking in ("1225", "1226"):
    feestdag = "Kerstmis"
else:
    feestdag = "No holiday found on given input."

# Outputs
print(f"{feestdag}")
