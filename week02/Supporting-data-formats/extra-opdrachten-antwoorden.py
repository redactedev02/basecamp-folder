"""Antwoorden bij extra-opdrachten.py (supporting topic Data formats, week 2).

Niet inleveren. Kijk hier pas in nadat je je eigen antwoord hebt opgeschreven.
Bij elk antwoord staat kort waarom het zo is. Dat "waarom" is wat je bij het
assessment moet kunnen vertellen, het antwoord zelf niet.

Run:  python extra-opdrachten-antwoorden.py
"""


def deel1_voorspel_de_output():
    print("=== Deel 1: voorspel de output ===")
    print("""
1.1  True
     0b1010 is geen ander getal dan 10, het is dezelfde waarde anders
     opgeschreven. De prefix 0b is iets van de broncode, niet van het getal.

1.2  False
     bin(10) geeft de string '0b1010', mét prefix. Vergelijken met '1010'
     is dus vergelijken met een kortere string.

1.3  0b1010b11
     bin(5) is '0b101' en bin(3) is '0b11'. Twee strings met + erachter
     elkaar geplakt, geen optelling. Wil je 5 + 3 binair, dan bin(5 + 3).

1.4  255
     int(tekst, 16) leest de tekst als hexadecimaal. ff is 15*16 + 15.

1.5  255
     int() accepteert de prefix 0x als het grondtal 16 is. Zelfde voor
     0b bij grondtal 2 en 0o bij grondtal 8.

1.6  ff
     hex(255) is de string '0xff', en [2:] snijdt de eerste twee tekens weg.
     Netter is f"{255:x}", want dat werkt ook als je opvulling wilt.

1.7  11111111
     08b betekent: binair, minstens 8 tekens breed, aanvullen met nullen,
     en zonder prefix. Precies wat je wilt als je bytes wilt laten zien.

1.8  0xa a A
     # zet de prefix erbij, x geeft kleine letters, X hoofdletters.

1.9  15 31 31
     0o17 is octaal (8 + 7), 0x1F is 31, 0b11111 is 31. Drie schrijfwijzen,
     Python print ze alledrie gewoon decimaal terug.

1.10 1020
     int("1010", 2) is 10, int("1010", 10) is 1010. Zelfde tekens, ander
     grondtal, totaal andere waarde. Hierom is dat tweede argument verplicht.

1.11 <class 'str'>
     bin() geeft een string terug, geen getal. Je kunt er niet mee rekenen
     voordat je hem met int(..., 2) terugleest.

1.12 10 11
     bin(255) is '0b11111111', dat is 2 tekens prefix plus 8 bits. bin(256)
     heeft er 9 nodig, want 256 past niet meer in een byte.

1.13 ValueError: invalid literal for int() with base 10: 'ff'
     Zonder tweede argument gaat int() uit van grondtal 10, en daar bestaat
     het cijfer f niet in.
""")


def deel2_handmatig_omrekenen():
    print("=== Deel 2: handmatig omrekenen ===")
    print("""
2.1  37 = 100101
     32 + 4 + 1.

2.2  96 = 1100000
     64 + 32.

2.3  130 = 10000010
     128 + 2.

2.4  511 = 111111111
     512 - 1, dus negen enen. Dit patroon is handig: 2**n - 1 is altijd n enen.

2.5  173 = AD
     Eerst binair: 128 + 32 + 8 + 4 + 1 = 10101101. Dan per 4 bits:
     1010 = A, 1101 = D.

2.6  4096 = 1000
     4096 is 2**12, en 12 bits zijn 3 hexcijfers. Een 1 gevolgd door drie nullen.

2.7  10110 = 22
     16 + 4 + 2.

2.8  11111110 = 254
     255 - 1, want alleen de laatste bit staat uit.

2.9  3C = 60
     3*16 + 12.

2.10 1A4 = 420
     1*256 + 10*16 + 4.

2.11 110110101100 = DAC
     Van rechts groeperen: 1101 1010 1100, dus D A C. Nooit via decimaal doen,
     dat is langer en foutgevoeliger.

2.12 9F = 10011111
     9 is 1001, F is 1111. Gewoon achter elkaar plakken.

2.13 Omdat 16 een macht van 2 is: 16 = 2**4, dus één hexcijfer is exact 4 bits
     en de grens tussen twee hexcijfers valt altijd precies op een bitgrens.
     10 is geen macht van 2, dus een decimaal cijfer dekt geen vast aantal bits
     en dan werkt groeperen niet.
""")


def deel3_schrijf_zelf():
    print("=== Deel 3: schrijf zelf ===")
    print("Dit zijn uitwerkingen, niet de enige goede oplossing.")
    print("Vergelijk met die van jou: doet die hetzelfde bij rare invoer?\n")

    print("--- 3.1 ---")
    getal = int(input("Geef een decimaal getal: "))
    print(f"{getal:08b}")
    # 08b doet het opvullen voor je. Zelf nullen plakken met "0" * (8 - len(...))
    # werkt ook, maar breekt zodra het getal groter is dan 255.

    print("--- 3.2 ---")
    a = input("Eerste hexadecimale getal: ")
    b = input("Tweede hexadecimale getal: ")
    verschil = int(a, 16) - int(b, 16)
    print("Decimaal:", verschil)
    print("Hexadecimaal:", hex(verschil))
    # Let op wat er gebeurt als b groter is dan a. hex(-10) geeft '-0xa'.
    # Een echte byte kan dat niet, die zou hier omklappen naar een hoge waarde.

    print("--- 3.3 ---")
    waarde = int(input("Geef een getal: "))
    if 0 <= waarde <= 255:
        print("Past in een unsigned byte.")
    elif -128 <= waarde <= 127:
        print("Past in een signed byte.")
    else:
        print("Past in geen van beide, hier heb je meer dan 1 byte voor nodig.")
    # De volgorde van de takken doet ertoe. 100 past in allebei, en deze code
    # noemt dan unsigned. Bedenk zelf of dat is wat je wilt.

    print("--- 3.4 ---")
    o1 = int(input("Octet 1: "))
    o2 = int(input("Octet 2: "))
    o3 = int(input("Octet 3: "))
    o4 = int(input("Octet 4: "))
    print(f"{o1:08b}.{o2:08b}.{o3:08b}.{o4:08b}")
    # Vier keer 8 bits is 32 bits, en dat is precies een IPv4-adres.

    print("--- 3.5 ---")
    print(naar_grondtal(255, 2), naar_grondtal(255, 8), naar_grondtal(255, 16))
    print("""
    def naar_grondtal(getal, grondtal):
        if grondtal == 2:
            return format(getal, "b")
        elif grondtal == 8:
            return format(getal, "o")
        elif grondtal == 16:
            return format(getal, "x")
        else:
            return str(getal)

    format() is bin()/oct()/hex() zonder prefix. De if/elif hier is nodig omdat
    Python geen ingebouwde functie heeft die een willekeurig grondtal doet,
    terwijl int(tekst, grondtal) de andere kant op wel elk grondtal van 2 tot 36 aankan.
    Dat is een mooie asymmetrie om te kunnen uitleggen.
""")


def naar_grondtal(getal, grondtal):
    if grondtal == 2:
        return format(getal, "b")
    elif grondtal == 8:
        return format(getal, "o")
    elif grondtal == 16:
        return format(getal, "x")
    else:
        return str(getal)


def deel4_bytes_en_endianness():
    print("=== Deel 4: bytes en endianness ===")
    print("""
4.1  0102
     258 is 256 + 2, dus byte 0x01 en byte 0x02. Big endian zet de zwaarste
     byte vooraan.

4.2  0201
     Zelfde getal, little endian, dus de lichtste byte vooraan. Intel- en
     AMD-processors doen dit, netwerkverkeer doet juist big endian.

4.3  256
     De eerste byte telt hier zwaar: 1 * 256 + 0.

4.4  1
     Dezelfde twee bytes, andere afspraak over de volgorde, andere waarde.
     Lees je bytes met de verkeerde endianness, dan krijg je geen foutmelding,
     alleen een verkeerd getal. Daarom staat het in bestandsformaten vastgelegd.

4.5  255
     Eén byte met alle bits aan, gelezen als unsigned.

4.6  -1
     Dezelfde byte, gelezen als signed. In two's complement is 11111111 gelijk
     aan -1. Signed of unsigned zit niet in de bits, dat is hoe jij ze leest.

4.7  ff
     Andersom hetzelfde verhaal: -1 opgeslagen in 1 signed byte is 0xff.

4.8  201
     2**200 heeft 201 bits nodig en Python doet daar niet moeilijk over.
     In C bestaat dit type niet, daar zou je een bibliotheek nodig hebben.

4.9  OverflowError: int too big to convert
     Hier zit precies het verschil. De int 256 mag bestaan, maar jij vraagt
     om hem in 1 byte te stoppen en daar passen maar 256 waarden in, 0 t/m 255.
     Python weigert dan, waar C stilletjes zou omklappen naar 0.

4.10 Endianness is de volgorde waarin de bytes van één getal in het geheugen of
     in een bestand staan. Aan het getal zelf verandert niets, alleen aan de
     opslag. Het gaat pas mis als de schrijver en de lezer een andere afspraak
     hanteren.
""")


def deel5_float_en_decimal():
    print("=== Deel 5: float en Decimal ===")
    print("""
5.1  0.30000000000000004
     0.1 en 0.2 zijn in binair oneindig repeterend, dus wat er in de float zit
     is net iets anders dan wat jij intikte. Bij het optellen wordt dat zichtbaar.

5.2  False
     En dit is waarom je floats nooit met == vergelijkt.

5.3  True
     Decimal rekent in grondtal 10, net als jij op papier. 0.1 is daar exact.

5.4  0.1000000000000000055511151231257827021181583404541015625
     Let op de ontbrekende aanhalingstekens. Decimal(0.1) krijgt eerst een float
     binnen, dus de fout zit er al in voordat Decimal begint. Altijd
     Decimal("0.1") met een string.

5.5  2.67
     Niet 2.68. De float die 2.675 heet, ligt in werkelijkheid net onder 2.675,
     dus naar beneden afronden is correct gedrag. In een boekhoudsysteem is dat
     een cent verschil, en over duizenden transacties loopt dat op.

5.6  0.5 is 2**-1, dus exact één bit. 0.25 en 0.125 ook. Alles wat je kunt
     schrijven als een som van machten van 2 past exact. 0.1 is 1/10 en 10 is
     geen macht van 2, dus dat wordt een repeterende breuk in binair, net zoals
     1/3 dat is in decimaal. Bij 64 bits kap je die ergens af, en dat is de fout.
""")


def deel6_uitleggen():
    print("=== Deel 6: uitleggen ===")
    print("""
6.1  bin(x) gaat van getal naar string, int(x, 2) van string naar getal.
     Elkaars omgekeerde, en alleen met het getal kun je rekenen.

6.2  Een byte is 8 bits, dus 2**8 = 256 verschillende waarden. Die beginnen bij
     0, dus de hoogste is 255. De klassieke afteller-fout zit hier.

6.3  255 is een int. "255" is een string van drie tekens. "0xFF" is een string
     van vier tekens die pas een getal wordt als jij int(..., 16) gebruikt.
     Python kiest dat grondtal nooit voor je.

6.4  Omdat 1 hexcijfer exact 4 bits is. Je kunt dus heen en weer zonder te
     rekenen, en 32 bits worden 8 leesbare tekens in plaats van 32 nullen en enen.

6.5  In C kies jij het type en heeft dat een vaste breedte, dus daar is "past
     niet meer in een char, gebruik een short" een echte keuze. Python heeft
     geen char en zijn int groeit gewoon door. Bij 256 gebeurt er niets
     bijzonders, het blijft een int, alleen is er intern een byte bijgekomen.

6.6  Zodra data naar buiten gaat: bytes, int.to_bytes(), de struct-module,
     bestanden, netwerksockets, numpy-dtypes. Daar kies je de breedte alsnog
     zelf, en daar krijg je ook een OverflowError als het niet past.

6.7  Omdat float in grondtal 2 rekent en geldbedragen in grondtal 10 zijn.
     Afrondfouten stapelen op over transacties, en een boekhouding die een cent
     mist klopt niet. Decimal rekent exact in grondtal 10 en laat je zelf de
     afrondregel kiezen.

6.8  Omdat een masker knipt op bitniveau, niet op cijferniveau. 255.255.255.0 is
     24 enen gevolgd door 8 nullen, en dan zie je meteen dat de eerste 24 bits
     het netwerk zijn en de laatste 8 de host. Bij een masker als 255.255.255.192
     is de decimale vorm betekenisloos en de binaire vorm (twee enen erbij)
     vertelt je direct dat je 4 subnetten van 64 adressen hebt.
""")


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
    keuze = input("Welk deel wil je nakijken? ")

    if keuze in DELEN:
        DELEN[keuze]()
    else:
        print("Dat deel bestaat niet. Kies 1 tot en met 6.")


if __name__ == "__main__":
    main()
