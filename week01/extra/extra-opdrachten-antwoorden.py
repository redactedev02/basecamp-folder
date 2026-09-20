"""Antwoorden bij extra-opdrachten.py (week 1, Python 01: Linear Programs).

Niet inleveren. Kijk hier pas in nadat je je eigen antwoord hebt opgeschreven.
Bij elk antwoord staat kort waarom het zo is. Dat "waarom" is wat je bij het
assessment moet kunnen vertellen, het antwoord zelf niet.

Run:  python extra-opdrachten-antwoorden.py
"""


def deel1_variabelen_en_toekenning():
    print("=== Deel 1: variabelen en toekenning ===")
    print("""
1.1  22 16
     b = a kopieert de waarde die a op dát moment heeft, namelijk 16. Dat a
     daarna 22 wordt verandert niets meer aan b. Er is geen blijvende band
     tussen de twee namen.

1.2  6 5
     Zelfde verhaal. q kreeg 5 en houdt 5, ook al gaat p daarna omhoog.

1.3  8
     Regel voor regel: 3, dan 3 * 3 = 9, dan 9 - 1 = 8. Bij x = x * x wordt
     rechts eerst uitgerekend met de oude waarde, pas daarna gaat het naar links.

1.4  aapnoot aap
     Strings werken hier net zo als getallen. s + "noot" maakt een nieuwe string
     en die gaat naar s. De string waar t naar wijst is niet aangepast, want
     strings zijn onveranderlijk (immutable).

1.5  12
     n += 5 is korter voor n = n + 5. 10 + 5 - 3.

1.6  True False
     5 == 5.0 is True, want het gaat om de waarde en int en float mag je
     vergelijken. "5" == 5 is False: tekst is geen getal, en Python rekent hier
     niets om. Let op: dit crasht niet, het geeft gewoon een fout antwoord.
     Dat soort bugs zijn lastiger dan een crash.

1.7  NameError: name 'prijs' is not defined
     Python leest van boven naar beneden. Op het moment van totaal = prijs * 2
     bestaat prijs nog niet. De volgorde van je regels is dus geen opmaak maar
     betekenis.

1.8  2naam mag niet, want een naam mag niet met een cijfer beginnen.
     mijn-naam mag niet, want het streepje is de min-operator; Python leest dat
     als mijn min naam. class mag niet, dat is een gereserveerd woord.
     naam2, mijn_naam, _naam en Naam mogen wel. Cijfers zijn dus prima, alleen
     niet als eerste teken. Naam en naam zijn twee verschillende variabelen,
     want Python is hoofdlettergevoelig.
""")


def deel2_types_en_conversie():
    print("=== Deel 2: types en conversie ===")
    print("""
2.1  <class 'int'> <class 'float'> <class 'str'> <class 'bool'>
     5 en 5.0 zijn verschillende types, ook al is de waarde gelijk.

2.2  10
     int("7") maakt van de tekst het getal 7, en dan is + optellen.

2.3  73
     Twee strings, dus + is plakken. Zelfde teken, andere betekenis, bepaald
     door het type van de operanden. Dit is de fout die je het vaakst maakt met
     invoer van de gebruiker.

2.4  7
     int() kapt af naar nul toe, het rondt niet af. int(7.9) is 7 en
     int(-7.9) is -7.

2.5  8 8
     Niet 8 en 9. round() in Python rondt een halve waarde af naar het dichtstbij-
     zijnde even getal (banker's rounding). Dat voorkomt dat je bij veel
     afrondingen structureel omhoog schuift.

2.6  4.5
     float("3.5") lukt wel, terwijl int("3.5") crasht. int() wil een hele tekst
     die een geheel getal is.

2.7  False False True True
     Leeg of nul is False, de rest is True. Let op "0": dat is een string met
     één teken erin, dus niet leeg, dus True.

2.8  <class 'float'>
     / geeft altijd een float terug, ook als het precies uitkomt. Wil je een
     int, gebruik dan //.

2.9  123
     Allebei omgezet naar tekst, dus plakken.

2.10 2
     bool is in Python een soort int: True is 1 en False is 0. Daarom kun je
     ermee rekenen en daarom is True + True gelijk aan 2.

2.11 ValueError: invalid literal for int() with base 10: '3.5'
     Het type klopt (het is tekst), maar de inhoud past niet bij wat int()
     verwacht. int(7.9) mag wel, want dat is al een getal en dan kapt Python af.
     Uit tekst wil hij geen aannames doen.

2.12 TypeError: can only concatenate str (not "int") to str
     Hier klopt het type zelf niet. Verschil met 2.11: ValueError betekent goed
     type, verkeerde inhoud. TypeError betekent verkeerd type. Oplossing is
     str(21) of een f-string.

2.13 input() geeft altijd een str. De gebruiker tikt tekens in en Python kan
     niet weten of "0612" een getal, een telefoonnummer of een code is. Zou
     Python zelf gokken, dan verloor je die informatie zonder het te merken.
     Jij bepaalt de betekenis met int() of float().
""")


def deel3_strings():
    print("=== Deel 3: strings ===")
    print("""
woord = "Rotterdam", posities 0 t/m 8.

3.1  R e m
     [0] is het eerste teken, [4] het vijfde (R-o-t-t-e), [-1] telt van achteren.

3.2  Rotte
     [0:5] is van 0 tot en met net niet 5, dus vijf tekens. Het einde ligt er
     altijd net buiten. Handig gevolg: het aantal tekens is einde min begin.

3.3  Rotdam
     [:3] is Rot en [-3:] is dam. Laat je begin of einde weg, dan neemt Python
     het uiteinde.

3.4  9

3.5  (een lege regel)
     [2:2] is van 2 tot net niet 2, dus nul tekens. Een lege string, geen fout.

3.6  3011 AB
     Dit is precies de postcodevraag uit de voorbereiding.

3.7  3333 12
     "3" * 4 herhaalt de tekst, 3 * 4 rekent. Weer hetzelfde teken met twee
     betekenissen, bepaald door het type.

3.8  HALLO hallo HaLLo
     Deze methodes wijzigen de string niet, ze geven een nieuwe terug. "Hallo"
     zelf blijft "Hallo", ook na .upper(). Wil je het bewaren, dan moet je het
     resultaat aan een variabele toekennen.

3.9  Hoi Sake, je naam heeft 4 letters
     Tussen de accolades mag elke expressie staan, dus ook len(naam).

3.10 3.14   7|    ab|
     .2f is twee decimalen, 3d is een getal in een vak van 3 breed
     (rechts uitgelijnd, dus twee spaties en dan de 7), en >5 is tekst in een vak
     van 5 rechts uitgelijnd. De print zet er zelf nog spaties tussen. Dit
     gebruik je om kolommen netjes onder elkaar te krijgen.

3.11 (een lege regel)
     Snijden buiten de string geeft gewoon niets terug.

3.12 IndexError: string index out of range
     Bij [9] vraag je één specifiek teken en dat bestaat niet, dus dat is een
     harde fout. Bij [9:] vraag je een reeks, en een lege reeks is een geldig
     antwoord. Python is streng waar het moet en soepel waar het kan.

3.13 Omdat de lengte van voornaam en achternaam per student verschilt, dus een
     vast getal als [15:21] klopt alleen bij jou. Robuuster is zoeken op een
     vast herkenningspunt: split("@") om het deel voor de apenstaart te pakken
     en dan split(".") om bij het laatste stuk te komen. Je leunt dan op de
     structuur van het adres in plaats van op de lengte.
""")


def deel4_rekenen():
    print("=== Deel 4: rekenen ===")
    print("""
4.1  3.5 3 1
     / is delen met kommagetal, // is de gehele deling (hoeveel keer past het
     helemaal), % is de rest. Samen beschrijven // en % de deling volledig.

4.2  1024
     ** is machtsverheffen. 2**10 is de reden dat 1 kB lang 1024 bytes heette.

4.3  14 20
     Keer gaat voor plus, tenzij je haakjes zet.

4.4  3
     Min is links-associatief: (10 - 4) - 3, niet 10 - (4 - 3).

4.5  512
     ** is als enige rechts-associatief: 2**(3**2) is 2**9. Niet 8**2 = 64.

4.6  1.5
     Delen gaat voor optellen, en het resultaat wordt een float zodra er één
     float bij komt kijken.

4.7  9
     9 // 2 * 2 is 8 (// en * zijn even sterk, dus van links naar rechts) en
     9 % 2 is 1. De gehele deling maal de deler plus de rest geeft altijd het
     oorspronkelijke getal terug. Dat is de definitie van een deling.

4.8  <class 'float'> <class 'int'>
     4 / 2 is 2.0 en niet 2. Print je een bedrag of een aantal, let dan op welke
     van de twee je wilt.

4.9  -4 1
     Niet -3 en -1. Python rondt bij // naar beneden af, ook bij negatieve
     getallen, en zorgt dat de rest hetzelfde teken heeft als de deler. In C en
     Java werkt dit anders, daar krijg je -3 en -1.

4.10 3 5
     % 10 geeft het laatste cijfer, // 10 % 10 het voorlaatste. Zo pel je een
     getal cijfer voor cijfer af zonder het naar tekst om te zetten.

4.11 ZeroDivisionError: division by zero. En ja, 5 % 0 crasht ook, met
     "integer modulo by zero", want de rest bij een deling door nul bestaat
     evenmin. Wil je dit voorkomen, dan moet je de deler controleren voordat je
     deelt, en dat is week 2 stof.

4.12 PEMDAS is Parentheses, Exponents, Multiplication/Division,
     Addition/Subtraction. Dat is dezelfde volgorde als "meneer van dalen wacht
     op antwoord", alleen zit machtsverheffen er expliciet in, direct na de
     haakjes en vóór keer en delen. Gelijk sterke operatoren gaan van links naar
     rechts, behalve **. Twijfel je, zet dan haakjes: die kosten niets en maken
     je bedoeling zichtbaar voor de volgende lezer.
""")


def deel5_schrijf_zelf():
    print("=== Deel 5: schrijf zelf ===")
    print("Uitwerkingen, niet de enige goede oplossing.")
    print("Vergelijk met die van jou: doet die hetzelfde bij rare invoer?\n")

    print("--- 5.1 ---")
    voornaam = input("Voornaam: ")
    achternaam = input("Achternaam: ")
    print(f"{voornaam[0].upper()}.{achternaam[0].upper()}.")
    # [0] pakt het eerste teken, .upper() vangt op dat iemand klein typt.
    # Denk na over een lege invoer: dan crasht [0] met een IndexError.

    print("--- 5.2 ---")
    postcode = input("Postcode (3011AB): ")
    print("Cijfers:", postcode[:4])
    print("Letters:", postcode[4:])

    print("--- 5.3 ---")
    celsius = float(input("Temperatuur in Celsius: "))
    fahrenheit = celsius * 9 / 5 + 32
    print(f"Dat is {fahrenheit:.1f} graden Fahrenheit.")
    # float() en niet int(), anders kun je geen 21.5 invoeren.
    # In 9 / 5 staat de deling vóór de + 32, dus haakjes zijn hier niet nodig.

    print("--- 5.4 ---")
    zin = input("Geef een zin: ")
    print("Aantal tekens zonder spaties:", len(zin.replace(" ", "")))
    # Eerst de spaties weghalen, dan pas tellen. Andersom werkt niet.

    print("--- 5.5 ---")
    centen = int(input("Aantal centen: "))
    print(f"{centen // 100} euro en {centen % 100} cent")
    # Dezelfde // en % als bij 4.7. Probeer 1205: dan zie je waarom je bij een
    # echte bon f"{centen % 100:02d}" wilt, anders staat er "5 cent".

    print("--- 5.6 ---")
    a = int(input("Deeltal: "))
    b = int(input("Deler: "))
    print(f"{a} gedeeld door {b} is {a // b} met rest {a % b}.")
    # Bij b = 0 crasht dit. Dat afvangen kan pas met if, volgende week.


def deel6_foutmeldingen():
    print("=== Deel 6: foutmeldingen ===")
    print("""
6.1  NameError: name 'voornaam' is not defined
     De naam bestaat niet. Meestal een typefout of een regel die je vergat.

6.2  TypeError: can only concatenate str (not "int") to str
     input() gaf een str terug en daar tel je een int bij op. Dit is de fout
     die iedereen in week 1 een keer maakt. Oplossing: int(input(...)).

6.3  ValueError: invalid literal for int() with base 10: 'twintig'
     Goed type, onmogelijke inhoud.

6.4  NameError: name 'Len' is not defined
     Python is hoofdlettergevoelig, de functie heet len. Merk op dat dit
     dezelfde fout is als 6.1: voor Python is Len gewoon een onbekende naam.

6.5  IndexError: string index out of range
     "abc" heeft posities 0, 1 en 2. Je vraagt om 5.

6.6  SyntaxError: '(' was never closed
     Een haakje dat nooit dichtgaat. Let op: de fout wijst vaak naar de regel
     eróna, want daar merkt Python pas dat het niet meer klopt. Zie je een
     SyntaxError die nergens op slaat, kijk dan een regel omhoog.

6.7  IndentationError: unexpected indent
     Inspringen betekent in Python "dit hoort bij het blok hierboven", en hier
     is er geen blok. Witruimte is dus onderdeel van de taal.

6.8  6.6 en 6.7 ziet Python al vóór het draaien. Dat zijn syntaxfouten: het
     bestand is geen geldige Python, dus er wordt geen enkele regel uitgevoerd,
     ook niet de regels erboven. De rest (NameError, TypeError, ValueError,
     IndexError) zijn runtime-fouten: de code is geldig, maar loopt tijdens het
     draaien vast. Je ziet dan wel de output van de regels die er al waren.
     Praktisch gevolg: een syntaxfout kun je niet "tot hier laten draaien".
""")


def deel7_uitleggen():
    print("=== Deel 7: uitleggen ===")
    print("""
7.1  Een waarde is de data zelf (42, "hallo"). Een variabele is een naam die
     naar die data verwijst. Dezelfde waarde kan meerdere namen hebben, en een
     naam kan later naar iets anders gaan wijzen.

7.2  = kent toe, == vergelijkt en levert True of False op. In een lineair
     programma gebruik je alleen =, vanaf week 2 komt == erbij.

7.3  input(). Die geeft altijd een str, ook als je 42 intikt. Voordat je kunt
     rekenen moet je omzetten met int() of float().

7.4  Letters, cijfers en underscores, niet beginnen met een cijfer, geen
     streepjes of spaties, geen gereserveerde woorden zoals class, if of for.
     Hoofdlettergevoelig. Cijfers mogen dus wel, alleen niet vooraan.

7.5  Ten eerste raak je de voorloopnul kwijt: 0612345678 als getal wordt
     612345678. Ten tweede reken je er nooit mee, en tekens als + of een spatie
     horen erbij. Hetzelfde geldt voor het huisnummer, want 8a is geen getal.
     Vuistregel: is het een code of een label, dan tekst. Ga je ermee rekenen,
     dan een getal.

7.6  7 / 2 is 3.5 (float), 7 // 2 is 3 (int). / deelt echt, // houdt alleen het
     hele deel over.

7.7  % geeft de rest van een deling. Gebruik je voor: even of oneven (n % 2),
     het laatste cijfer van een getal (n % 10), en om een grote eenheid op te
     splitsen in kleinere, zoals centen naar euro's of seconden naar minuten.

7.8  Een string met een f ervoor, waarin je tussen accolades een expressie mag
     zetten. Voordelen boven print("a", b, "c"): je bepaalt zelf waar spaties
     staan, je kunt opmaak meegeven zoals .2f, en je ziet in één blik hoe de zin
     eruit komt te zien.

7.9  Precedence is de volgorde waarin operatoren aan de beurt komen. Zonder die
     afspraak zou 2 + 3 * 4 zowel 14 als 20 kunnen zijn. Haakjes overrulen de
     volgorde en maken je bedoeling expliciet.

7.10 Een programma dat van boven naar beneden in één rechte lijn loopt, zonder
     keuzes en zonder herhaling. Drie blokken: invoer, verwerking, uitvoer. Die
     scheiding is ook hoe je een opdracht aanpakt: eerst opschrijven wat er
     binnenkomt en wat eruit moet, dan pas de berekening ertussen.

7.11 Kijk naar de onderste regel van de traceback: daar staat het type fout en
     wat Python verwachtte. Kijk daarboven naar het regelnummer. Print dan de
     variabele die daar staat samen met type(...) ervan. Bijna altijd blijkt
     iets een str te zijn waar jij een int in dacht te hebben.
""")


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
    keuze = input("Welk deel wil je nakijken? ")

    if keuze in DELEN:
        DELEN[keuze]()
    else:
        print("Dat deel bestaat niet. Kies 1 tot en met 7.")


if __name__ == "__main__":
    main()
