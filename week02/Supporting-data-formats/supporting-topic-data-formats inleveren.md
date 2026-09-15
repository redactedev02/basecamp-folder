# Supporting topic — Data formats (Arch 1)

## 2.1 Supporting topic week 2 – Data formats

Handmatig omrekenen

Cijfers in decimale getallen zijn 0-9. Wat zijn de cijfers in hexadecimaal formaat? Wat zijn de cijfers in binair formaat?

| Decimaal     | 0        | 1        | 2        | 3        | 4        | 5        | 6        | 7        | 8        | 9        |
| ------------ | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- | -------- |
| Hexadecimaal |  0       |    1     |    2     |    3     | 4        | 5        | 6        | 7        | 8        | 9        |
| Binair       | 00000000 | 00000001 | 00000010 | 00000011 | 00000100 | 00000101 | 00000110 | 00000111 | 00001000 | 00001001 |

Converteer (handmatig) de volgende decimale getallen naar hexadecimaal en binair: 8, 10, 15, 21, 32, 64, 256, 500, 512, 1000.

| Decimaal     | 8        | 10       | 15       | 21       | 32       | 64       | 256              | 500              | 512              | 1000             |
| ------------ | -------- | -------- | -------- | -------- | -------- | -------- | ---------------- | ---------------- | ---------------- | ---------------- |
| Hexadecimaal | 8        | A        | F        | 15       | 20       | 40       | 100              | 1F4              | 200              | 3E8              |
| Binair       | 00001000 | 00001010 | 00001111 | 00010101 | 00100000 | 01000000 | 0000000100000000 | 0000000111110100 | 0000001000000000 | 0000001111101000 |


### 04 Hoe geeft Python deze data formats weer? Hoe kun je Python gebruiken om deze data forms naar elkaar te converteren?
bin(), oct() en hex(), en geven een string. Omzetten van tekst naar getal doe je met int(tekst, grondtal)

### Omrekenen in Python



#### Converteer het decimale getal 45 naar zijn binaire weergave.

```python
getal = int(input("Geef een decimaal getal: "))
print("Binair:", bin(getal))
```

```
Input:  45
Output: Binair: 0b101101

```
#### Zet het binaire getal 1010101 om in decimale vorm.

```python
binair = input("Geef een binair getal: ")
print("Decimaal:", int(binair, 2))
```

```
Input:  1010101
Output: Decimaal: 85

```
#### Tel de binaire getallen 10111 en 1101 bij elkaar op en druk het resultaat uit in 0binaire vorm.

```python
a = input("Eerste binaire getal: ")
b = input("Tweede binaire getal: ")
som = int(a, 2) + int(b, 2)
print("Som binair:", bin(som))
```

```
Input:  10111 en 1101
Output: Som binair: 0b100100
```

#### Zet het decimale getal 255 om in zijn hexadecimale vorm.

```python
getal = int(input("Geef een decimaal getal: "))
print("Hexadecimaal:", hex(getal))
```

```
Input:  255
Output: Hexadecimaal: 0xff
```

#### Converteer het hexadecimale getal 2A in decimale vorm.

```python
hexa = input("Geef een hexadecimaal getal: ")
print("Decimaal:", int(hexa, 16))
```

```
Input:  2A
Output: Decimaal: 42
```

#### Tel de hexadecimale getallen C4 en 3A bij elkaar op en druk het resultaat uit in hexadecimaal.

```python
a = input("Eerste hexadecimale getal: ")
b = input("Tweede hexadecimale getal: ")
som = int(a, 16) + int(b, 16)
print("Som hexadecimaal:", hex(som))
```

```
Input:  C4 en 3A
Output: Som hexadecimaal: 0xfe
```

#### Converteer het binaire getal 1101 in decimale vorm.

```python
binair = input("Geef een binair getal: ")
print("Decimaal:", int(binair, 2))
```

```
Input:  1101
Output: Decimaal: 13
```

#### Converteer het hexadecimale getal F0 in decimale vorm.

```python
hexa = input("Geef een hexadecimaal getal: ")
print("Decimaal:", int(hexa, 16))
```

```
Input:  F0
Output: Decimaal: 240
```

#### Tel de decimale getallen 123 en 456 bij elkaar op.

```python
a = int(input("Eerste getal: "))
b = int(input("Tweede getal: "))
print("Som:", a + b)
```

```
Input:  123 en 456
Output: Som: 579
```

#### Converteer het decimale getal 157 naar binair en vervolgens naar hexadecimaal.

```python
getal = int(input("Geef een decimaal getal: "))
print("Binair:", bin(getal))
print("Hexadecimaal:", hex(getal))
```

```
Input:  157
Output: Binair: 0b10011101
        Hexadecimaal: 0x9d
```

#### Converteer het binaire getal 11101101 in decimale en vervolgens in hexadecimale vorm.

```python
binair = input("Geef een binair getal: ")
getal = int(binair, 2)
print("Decimaal:", getal)
print("Hexadecimaal:", hex(getal))
```

```
Input:  11101101
Output: Decimaal: 237
        Hexadecimaal: 0xed
```

#### Converteer het hexadecimale getal AB4 in decimaal en vervolgens in binair.

```python
hexa = input("Geef een hexadecimaal getal: ")
getal = int(hexa, 16)
print("Decimaal:", getal)
print("Binair:", bin(getal))
```

```
Input:  AB4
Output: Decimaal: 2740
        Binair: 0b101010110100
```

## Toepassingen in de praktijk

#### Ga op onderzoek uit en geef hieronder een voorbeeld uit de praktijk waarbij binaire gegevens veelvuldig worden gebruikt.

Met netwerken, ip-adressen zijn 32bits opgedeeld in vier bytes. Subnetmaskers zijn juist binair.

Veel bestandsformaten zijn binair zoals .png en .jpg.

#### Onderzoek hoe hexadecimaal wordt gebruikt bij het aanspreken van het computergeheugen. Leg het kort in je eigen woorden uit.

Geheugenadressen zijn binaire getallen, een 64-bits adres is onleesbaar om op te schrijven, daarom word daar hexadecimaal gebruikt. Het is een goede tussenvorm omdat 1 hexcijfer uit 4 bits bestaat. Je kunt snel en makkelijker doorrekenen dan vanuit decimaal, omdat die het grondgetal heeft van 10, dat is geen macht van 2.

#### Onderzoek hoe decimale gegevensformaten worden gebruikt in financiële berekeningen of boekhoudsystemen. Leg het kort in je eigen woorden uit.

Computers saan kommagetallen als een binair float, het probleem is dan dat 0,1 een oneindig wordt, net als 1/3 bijvoorbeeld. Die afwijking wordt steeds groter met meer transacties. Daarom gebruiken ze een decimaal formaat met: from decimal import Decimal.

#### Van welke bronnen heb je gebruik gemaakt bij het doen van onderzoek (websites, boeken, artikelen). Geef hier de door jouw gebruikte bronnen weer.

- https://docs.python.org/3/library/functions.html
- https://www.youtube.com/watch?v=TP9OCX-kZuc
- https://www.youtube.com/watch?v=qL8jSyc_L2c
- https://www.youtube.com/watch?v=WhOAjATrpOw
- https://www.khanacademy.org/math/algebra-home/alg-intro-to-algebra/algebra-alternate-number-bases/v/binary-to-hexadecimal
