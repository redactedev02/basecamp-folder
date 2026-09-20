# A1W2A1 - Swimming tickets
# Description: see README.md in this folder
# Deadline: 2027-01-08 23:59 (CET)

# Inputs
subscription = input("How much does the subscription cost?")
single_ticket = input("How much does a single ticket cost?")
visits = input("How many visits will you make?")

# Processing

# int en float
subscription = float(subscription)
single_ticket = float(single_ticket)
visits = int(visits)


# Totale prijs berekenen met single tickets
total_single = single_ticket * visits

# besparing uitrekenen
savings = total_single - subscription


# Outputs
# if else, =< voor zelfde prijs; dan enkele tickets
if total_single <= subscription:
    print(f"Single tickets: €{total_single:.1f}")
    print(f"Monthly subscription: €{subscription:.1f}")
    print("Advice: Buy single tickets")
else:
    print(f"Single tickets: €{total_single:.1f}")
    print(f"Monthly subscription: €{subscription:.1f}")
    print("Advice: Buy a subscription")
    print(f"You save €{savings:.1f}")
