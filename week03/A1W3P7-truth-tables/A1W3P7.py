# A1W3P7 - Truth tables
# Description: see README.md in this folder
# Deadline: 2026-09-25 23:59 (CEST)

values = [True, False]

# processing
# loop in loop met 2 opties = 2*2
print("AND")
for a in values:
    for b in values:
        print(a, "+", b, "=", a and b)

print()

print("OR")
for a in values:
    for b in values:
        print(a, "+", b, "=", a or b)
