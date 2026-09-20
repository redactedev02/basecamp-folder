"""Extra oefenopgaven bij het supporting topic Data formats (week 2).

Niet inleveren. Dit is oefenmateriaal om te testen of de theorie echt zit:
talstelsels, bits en bytes, signed en unsigned, endianness, en het verschil
tussen een getal en de weergave van dat getal.

Werkwijze
1. Schrijf je antwoord eerst op achter "Jouw antwoord:" hieronder in dit bestand.
2. Run daarna dat deel en vergelijk met wat Python zegt.
3. Klopt het niet, zoek dan eerst uit waarom voordat je de antwoorden opent.

Antwoorden: extra-opdrachten-antwoorden.py
Run:        python extra-opdrachten.py
"""


def deel1_voorspel_de_output():
    """Wat print Python? Eerst opschrijven, dan pas runnen.

    Dit deel gaat over een ding: een getal heeft geen talstelsel, alleen de
    weergave ervan heeft dat.
    """
    print("=== Deel 1: voorspel de output ===")

    # 1.1  Jouw antwoord:
    print("1.1 ->", 0b1010 == 10)

    # 1.2  Jouw antwoord:
    print("1.2 ->", bin(10) == "1010")
    print(bin(10))

    # 1.3  Jouw antwoord:
    print("1.3 ->", bin(5) + bin(3))

    # 1.4  Jouw antwoord:
    print("1.4 ->", int("ff", 16))

    # 1.5  Jouw antwoord:
    print("1.5 ->", int("0xff", 16))

    # 1.6  Jouw antwoord:
    print("1.6 ->", hex(255)[2:])

    # 1.7  Jouw antwoord:
    print("1.7 ->", f"{255:08b}")

    # 1.8  Jouw antwoord:
    print("1.8 ->", f"{10:#x}", f"{10:x}", f"{10:X}")

    # 1.9  Jouw antwoord:
    print("1.9 ->", 0o17, 0x1F, 0b11111)

    # 1.10  Jouw antwoord:
    print("1.10 ->", int("1010", 2) + int("1010", 10))

    # 1.11  Jouw antwoord:
    print("1.11 ->", type(bin(4)))

    # 1.12  Jouw antwoord:
    print("1.12 ->", len(bin(255)), len(bin(256)))

    # 1.13  Deze regel crasht. Welke fout krijg je, en waarom?
    #       Jouw antwoord:
    #       Haal het commentaar eronder weg om het te controleren.
    # print("1.13 ->", int("ff"))


def deel2_handmatig_omrekenen():
    """Pen en papier. Geen rekenmachine, geen Python.

    Methode: aftrekken van machten van 2 (1 2 4 8 16 32 64 128 256 512 1024),
    en tussen binair en hex groepeer je per 4 bits vanaf rechts.
    """
    print("=== Deel 2: handmatig omrekenen ===")
    print("Dit deel maak je op papier. Antwoorden invullen in dit bestand.")

    # 2.1  Decimaal naar binair: 37
    #      Jouw antwoord:

    # 2.2  Decimaal naar binair: 96
    #      Jouw antwoord:

    # 2.3  Decimaal naar binair: 130
    #      Jouw antwoord:

    # 2.4  Decimaal naar binair: 511
    #      Jouw antwoord:

    # 2.5  Decimaal naar hexadecimaal: 173
    #      Jouw antwoord:

    # 2.6  Decimaal naar hexadecimaal: 4096
    #      Jouw antwoord:

    # 2.7  Binair naar decimaal: 10110
    #      Jouw antwoord:

    # 2.8  Binair naar decimaal: 11111110
    #      Jouw antwoord:

    # 2.9  Hexadecimaal naar decimaal: 3C
    #      Jouw antwoord:

    # 2.10 Hexadecimaal naar decimaal: 1A4
    #      Jouw antwoord:

    # 2.11 Binair direct naar hexadecimaal, zonder via decimaal: 110110101100
    #      Jouw antwoord:

    # 2.12 Hexadecimaal direct naar binair, zonder via decimaal: 9F
    #      Jouw antwoord:

    # 2.13 Waarom kan die groepering per 4 bits bij hex wel, en bij decimaal niet?
    #      Jouw antwoord:


def deel3_schrijf_zelf():
    """Kleine programma's. Andere problemen dan je supporting topic.

    Schrijf ze onder de opdracht in dit bestand, of in een eigen kladbestand.
    """
    print("=== Deel 3: schrijf zelf ===")

    # 3.1  Vraag een decimaal getal en print het als binair van precies 8 tekens,
    #      zonder de 0b-prefix. Dus 5 wordt 00000101.

    # 3.2  Vraag twee hexadecimale getallen en print het verschil, zowel decimaal
    #      als hexadecimaal.

    # 3.3  Vraag een getal en print of het in een unsigned byte past (0 t/m 255),
    #      in een signed byte (-128 t/m 127), of in geen van beide.

    # 3.4  Vraag de vier octetten van een IPv4-adres en print het volledige adres
    #      als 32 bits, met een punt tussen elke groep van 8.
    #      192.168.1.1 wordt 11000000.10101000.00000001.00000001

    # 3.5  Schrijf een functie die een getal en een grondtal krijgt en de weergave
    #      teruggeeft zonder prefix. Laat hem werken voor grondtal 2, 8 en 16.


def deel4_bytes_en_endianness():
    """Hier worden byte-breedtes in Python pas echt zichtbaar.

    Een int in Python groeit onbeperkt. Zodra je naar bytes gaat, kies je zelf
    de breedte en de volgorde, en dan gelden de grenzen uit de theorie weer.
    """
    print("=== Deel 4: bytes en endianness ===")

    # 4.1  Jouw antwoord:
    print("4.1 ->", (258).to_bytes(2, "big").hex())

    # 4.2  Jouw antwoord:
    print("4.2 ->", (258).to_bytes(2, "little").hex())

    # 4.3  Jouw antwoord:
    print("4.3 ->", int.from_bytes(b"\x01\x00", "big"))

    # 4.4  Jouw antwoord:
    print("4.4 ->", int.from_bytes(b"\x01\x00", "little"))

    # 4.5  Jouw antwoord:
    print("4.5 ->", int.from_bytes(b"\xff", "big"))

    # 4.6  Jouw antwoord:
    print("4.6 ->", int.from_bytes(b"\xff", "big", signed=True))

    # 4.7  Jouw antwoord:
    print("4.7 ->", (-1).to_bytes(1, "big", signed=True).hex())

    # 4.8  Jouw antwoord:
    print("4.8 ->", (2**200).bit_length())

    # 4.9  Deze regel crasht. Welke fout, en waarom is dat precies het verschil
    #      tussen een int en een byte?
    #      Jouw antwoord:
    # print("4.9 ->", (256).to_bytes(1, "big"))

    # 4.10 Wat is endianness, en wat verandert er aan het getal zelf als je van
    #      big naar little endian gaat?
    #      Jouw antwoord:


def deel5_float_en_decimal():
    """Waarom geld niet in floats gaat."""
    print("=== Deel 5: float en Decimal ===")

    from decimal import Decimal

    # 5.1  Jouw antwoord:
    print("5.1 ->", 0.1 + 0.2)

    # 5.2  Jouw antwoord:
    print("5.2 ->", 0.1 + 0.2 == 0.3)

    # 5.3  Jouw antwoord:
    print("5.3 ->", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))

    # 5.4  Let op de aanhalingstekens. Jouw antwoord:
    print("5.4 ->", Decimal(0.1))

    # 5.5  Jouw antwoord:
    print("5.5 ->", round(2.675, 2))

    # 5.6  Waarom gaat 0.1 in binair mis, en 0.5 niet?
    #      Jouw antwoord:


def deel6_uitleggen():
    """Mondelinge vragen. Hardop beantwoorden, zonder naar code te kijken."""
    print("=== Deel 6: uitleggen ===")

    # 6.1  Wat is het verschil tussen bin(x) en int(x, 2)?
    # 6.2  Waarom loopt een unsigned byte tot 255 en niet tot 256?
    # 6.3  Wat is het verschil tussen 255 en "255" en "0xFF" voor Python?
    # 6.4  Waarom is hex handiger dan decimaal om bits mee op te schrijven?
    # 6.5  Waarom is "een getal groter dan 255 wordt een short" een uitspraak over
    #      C en niet over Python? Wat gebeurt er in Python bij 256?
    # 6.6  Waar in Python zie je byte-breedtes wel terug?
    # 6.7  Waarom gebruiken boekhoudsystemen Decimal in plaats van float?
    # 6.8  Een subnetmasker is 255.255.255.0. Waarom is dat binair makkelijker te
    #      begrijpen dan decimaal?


DELEN = {
    "1": deel1_voorspel_de_output,
    "2": deel2_handmatig_omrekenen,
    "3": deel3_schrijf_zelf,
    "4": deel4_bytes_en_endianness,
    "5": deel5_float_en_decimal,
    "6": deel6_uitleggen,
}


def main():
    print(__doc__)
    print("1 voorspel de output   2 handmatig omrekenen   3 schrijf zelf")
    print("4 bytes en endianness  5 float en Decimal      6 uitleggen")
    keuze = input("Welk deel wil je runnen? ")

    if keuze in DELEN:
        DELEN[keuze]()
    else:
        print("Dat deel bestaat niet. Kies 1 tot en met 6.")


if __name__ == "__main__":
    main()
