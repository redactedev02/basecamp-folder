# A1W2A1 - Swimming tickets

# Inputs
subscription = input("Enter subscription: ")
single_ticket = input("Enter single ticket: ")
visits = input("Enter number of visits: ")


# Validatie
def validate_int(input_str: str) -> bool:
    if input_str.isdigit():
        return True
    else:
        print("Invalid input")
        return False


def validate_float(input_str: str) -> bool:
    parts = input_str.split(".")
    if (
        len(parts) == 1
        and parts[0].isdigit()
        or len(parts) == 2
        and parts[0].isdigit()
        and parts[1].isdigit()
    ):
        return True
    else:
        print("Invalid input")
        return False


# valideren, daarna omzetten en rekenen
if (
    validate_float(subscription)
    and validate_float(single_ticket)
    and validate_int(visits)
):
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
    # if else, <= voor zelfde prijs; dan enkele tickets
    if total_single <= subscription:
        print(f"Single tickets: €{total_single:.1f}")
        print(f"Monthly subscription: €{subscription:.1f}")
        print("Advice: Buy single tickets")
    else:
        print(f"Single tickets: €{total_single:.1f}")
        print(f"Monthly subscription: €{subscription:.1f}")
        print("Advice: Buy a subscription")
        print(f"You save €{savings:.1f}")
