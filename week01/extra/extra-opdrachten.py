"""Extra oefenopgaven bij week 1: Python 01, Linear Programs.

Niet inleveren. Dit dekt wat je in week 1 moest leren: waarden en variabelen,
primitieve types, strings, rekenen, type-conversie, en het lezen van
foutmeldingen. Een lineair programma is een rechte lijn van invoer naar
verwerking naar uitvoer, zonder keuzes en zonder herhaling.

Werkwijze
1. Schrijf je antwoord eerst op achter "Jouw antwoord:" hieronder in dit bestand.
2. Run daarna dat deel en vergelijk met wat Python zegt.
3. Klopt het niet, zoek dan eerst uit waarom voordat je de antwoorden opent.

Antwoorden: extra-opdrachten-antwoorden.py
Run:        python extra-opdrachten.py
"""


def deel1_variabelen_en_toekenning():
    """Wat staat er in welke variabele, en wanneer?

    Het draait om één ding: = is geen gelijkteken maar een opdracht.
    Rechts wordt eerst uitgerekend, daarna gaat het resultaat naar links.
    """
    print("=== Deel 1: variabelen en toekenning ===")

    # 1.1  Jouw antwoord:
    a = 16
    b = 12
    b = a
    a = 22
    print("1.1 ->", a, b)

    # 1.2  Jouw antwoord:
    p = 5
    q = p
    p = p + 1
    print("1.2 ->", p, q)

    # 1.3  Jouw antwoord:
    x = 3
    x = x * x
    x = x - 1
    print("1.3 ->", x)

    # 1.4  Jouw antwoord:
    s = "aap"
    t = s
    s = s + "noot"
    print("1.4 ->", s, t)

    # 1.5  Jouw antwoord:
    n = 10
    n += 5
    n -= 3
    print("1.5 ->", n)

    # 1.6  Jouw antwoord:
    print("1.6 ->", 5 == 5.0, "5" == 5)

    # 1.7  Deze regel crasht. Welke fout, en wat zegt die over de volgorde
    #      waarin Python een toekenning leest?
    #      Jouw antwoord:
    # totaal = prijs * 2
    # prijs = 10

    # 1.8  Welke van deze namen mag niet in Python, en waarom precies?
    #      naam2 / 2naam / mijn_naam / mijn-naam / _naam / class / Naam
    #      Jouw antwoord:


def deel2_types_en_conversie():
    """Elk waarde heeft een type, en het type bepaalt wat + betekent."""
    print("=== Deel 2: types en conversie ===")

    # 2.1  Jouw antwoord:
    print("2.1 ->", type(5), type(5.0), type("5"), type(True))

    # 2.2  Jouw antwoord:
    print("2.2 ->", int("7") + 3)

    # 2.3  Jouw antwoord:
    print("2.3 ->", "7" + "3")

    # 2.4  Jouw antwoord:
    print("2.4 ->", int(7.9))

    # 2.5  Jouw antwoord:
    print("2.5 ->", round(7.5), round(8.5))

    # 2.6  Jouw antwoord:
    print("2.6 ->", float("3.5") + 1)

    # 2.7  Jouw antwoord:
    print("2.7 ->", bool(0), bool(""), bool("0"), bool(-1))

    # 2.8  Jouw antwoord:
    print("2.8 ->", type(10 / 2))

    # 2.9  Jouw antwoord:
    print("2.9 ->", str(12) + str(3))

    # 2.10 Jouw antwoord:
    print("2.10 ->", int(True) + int(True))

    # 2.11 Deze regel crasht. Welke fout, en waarom is int(7.9) wel toegestaan?
    #      Jouw antwoord:
    # print("2.11 ->", int("3.5"))

    # 2.12 Deze regel crasht ook, maar met een andere fout. Welke, en wat is het
    #      verschil met 2.11?
    #      Jouw antwoord:
    # print("2.12 ->", "leeftijd: " + 21)

    # 2.13 input() geeft altijd hetzelfde type terug, wat je ook intikt.
    #      Welk type, en waarom heeft Python dat zo gedaan?
    #      Jouw antwoord:


def deel3_strings():
    """Tellen begint bij 0. Snijden gaat tot en met net niet."""
    print("=== Deel 3: strings ===")

    woord = "Rotterdam"

    # 3.1  Jouw antwoord:
    print("3.1 ->", woord[0], woord[4], woord[-1])

    # 3.2  Jouw antwoord:
    print("3.2 ->", woord[0:5])

    # 3.3  Jouw antwoord:
    print("3.3 ->", woord[:3] + woord[-3:])

    # 3.4  Jouw antwoord:
    print("3.4 ->", len(woord))

    # 3.5  Jouw antwoord:
    print("3.5 ->", woord[2:2])

    # 3.6  Jouw antwoord:
    postcode = "3011AB"
    print("3.6 ->", postcode[:4], postcode[4:])

    # 3.7  Jouw antwoord:
    print("3.7 ->", "3" * 4, 3 * 4)

    # 3.8  Jouw antwoord:
    print("3.8 ->", "Hallo".upper(), "Hallo".lower(), "Hallo".replace("l", "L"))

    # 3.9  Jouw antwoord:
    naam = "Sake"
    print("3.9 ->", f"Hoi {naam}, je naam heeft {len(naam)} letters")

    # 3.10 Jouw antwoord:
    print("3.10 ->", f"{3.14159:.2f}", f"{7:3d}|", f"{'ab':>5}|")

    # 3.11 Jouw antwoord:
    print("3.11 ->", woord[9:])

    # 3.12 Deze regel crasht, terwijl 3.11 dat niet deed. Waarom is snijden
    #      buiten de string wel toegestaan en er één teken uit pakken niet?
    #      Jouw antwoord:
    # print("3.12 ->", woord[9])

    # 3.13 Je schoolmail is voornaam.achternaam.123456@hr.nl en je wilt alleen
    #      het studentnummer. Waarom is slicing met vaste getallen hier riskant,
    #      en wat zou je in plaats daarvan gebruiken?
    #      Jouw antwoord:


def deel4_rekenen():
    """Operatoren, voorrang, en het verschil tussen / en //."""
    print("=== Deel 4: rekenen ===")

    # 4.1  Jouw antwoord:
    print("4.1 ->", 7 / 2, 7 // 2, 7 % 2)

    # 4.2  Jouw antwoord:
    print("4.2 ->", 2**10)

    # 4.3  Jouw antwoord:
    print("4.3 ->", 2 + 3 * 4, (2 + 3) * 4)

    # 4.4  Jouw antwoord:
    print("4.4 ->", 10 - 4 - 3)

    # 4.5  Jouw antwoord:
    print("4.5 ->", 2**3**2)

    # 4.6  Jouw antwoord:
    print("4.6 ->", 1 + 2 / 4)

    # 4.7  Jouw antwoord:
    print("4.7 ->", 9 // 2 * 2 + 9 % 2)

    # 4.8  Jouw antwoord:
    print("4.8 ->", type(4 / 2), type(4 // 2))

    # 4.9  Jouw antwoord:
    print("4.9 ->", -7 // 2, -7 % 2)

    # 4.10 Jouw antwoord:
    print("4.10 ->", 153 % 10, 153 // 10 % 10)

    # 4.11 Deze regel crasht. Welke fout, en crasht 5 % 0 ook?
    #      Jouw antwoord:
    # print("4.11 ->", 5 / 0)

    # 4.12 PEMDAS of "meneer van dalen": waar zit het verschil met hoe jij het
    #      op de middelbare school leerde, en waar zit ** in die volgorde?
    #      Jouw antwoord:


def deel5_schrijf_zelf():
    """Lineaire programma's. Andere problemen dan je weekopdrachten.

    Houd de vorm aan uit template.py: eerst invoer, dan verwerking, dan uitvoer,
    met een lege regel ertussen. Dat is de structuur waar je op beoordeeld wordt.
    """
    print("=== Deel 5: schrijf zelf ===")

    # 5.1  Vraag voornaam en achternaam en print de initialen met punten.
    #      "sake" en "bakker" wordt S.B.

    # 5.2  Vraag een postcode in de vorm 3011AB en print de cijfers en de letters
    #      op twee aparte regels.

    # 5.3  Vraag een temperatuur in graden Celsius en print de waarde in
    #      Fahrenheit, afgerond op 1 decimaal. De formule is F = C * 9 / 5 + 32.

    # 5.4  Vraag een zin en print hoeveel tekens die heeft zonder de spaties.

    # 5.5  Vraag een aantal centen en print het als euro's en centen.
    #      1234 wordt "12 euro en 34 cent".

    # 5.6  Vraag twee getallen en print de gehele deling en de rest in één zin,
    #      met een f-string.


def deel6_foutmeldingen():
    """Een foutmelding lees je van onder naar boven: eerst het type, dan de regel.

    Voorspel per geval welk type fout je krijgt. Haal daarna het commentaar weg
    en controleer het. Zet het commentaar er weer voor, anders crasht het deel
    op het eerste geval.
    """
    print("=== Deel 6: foutmeldingen ===")

    # 6.1  Jouw antwoord:
    # print(voornaam)

    # 6.2  Jouw antwoord:
    # leeftijd = input("Leeftijd: ")
    # print(leeftijd + 1)

    # 6.3  Jouw antwoord:
    # print(int("twintig"))

    # 6.4  Jouw antwoord:
    # print(Len("abc"))

    # 6.5  Jouw antwoord:
    # print("abc"[5])

    # 6.6  Jouw antwoord:
    # print("hoi"

    # 6.7  Jouw antwoord:
    # prijs = 10
    #   aantal = 3

    # 6.8  Welke van deze zeven fouten ziet Python al voordat het programma
    #      begint te draaien, en welke pas tijdens het draaien?
    #      Jouw antwoord:


def deel7_uitleggen():
    """Mondelinge vragen. Hardop beantwoorden, zonder naar code te kijken."""
    print("=== Deel 7: uitleggen ===")

    # 7.1  Wat is het verschil tussen een waarde en een variabele?
    # 7.2  Wat is het verschil tussen = en ==?
    # 7.3  Welke functie leest invoer van de gebruiker, en welk type geeft die
    #      altijd terug? Wat moet je dus doen voordat je ermee kunt rekenen?
    # 7.4  Welke regels gelden er voor een variabelenaam in Python? Mogen er
    #      cijfers in?
    # 7.5  Waarom sla je een telefoonnummer op als tekst en niet als getal?
    #      Noem twee redenen.
    # 7.6  Wat is het verschil tussen 7 / 2 en 7 // 2, en welk type komt eruit?
    # 7.7  Wat doet % en waar gebruik je dat voor?
    # 7.8  Wat is een f-string en wat is het voordeel boven print("a", b, "c")?
    # 7.9  Wat betekent precedence en waarom heb je haakjes nodig?
    # 7.10 Wat is een lineair programma, en welke drie blokken heeft het?
    # 7.11 Je programma crasht met TypeError. Wat is je eerste stap om te zien
    #      welke aanname van jou niet klopt?


DELEN = {
    "1": deel1_variabelen_en_toekenning,
    "2": deel2_types_en_conversie,
    "3": deel3_strings,
    "4": deel4_rekenen,
    "5": deel5_schrijf_zelf,
    "6": deel6_foutmeldingen,
    "7": deel7_uitleggen,
}


def main():
    print(__doc__)
    print("1 variabelen en toekenning  2 types en conversie  3 strings")
    print("4 rekenen                   5 schrijf zelf        6 foutmeldingen")
    print("7 uitleggen")
    keuze = input("Welk deel wil je runnen? ")

    if keuze in DELEN:
        DELEN[keuze]()
    else:
        print("Dat deel bestaat niet. Kies 1 tot en met 7.")


if __name__ == "__main__":
    main()
