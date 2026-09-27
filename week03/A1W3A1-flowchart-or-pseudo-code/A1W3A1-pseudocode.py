# A1W3A1 — Flowchart or pseudo-code

Deliverable: a flowchart **or** pseudo-code for `A1W3A2 - Mountain climbing time trail`.
See README.md in this folder for the full assignment.

## Pseudo-code

# Helper functies
Input naam
  herhaal
  Voorwaarden, mag niet: korter dan len(1) langer dan len(9), getallen bevatten, beginnen met hoofdletter (Valideren met bool), andere dingen dan letters
  tot name is geldig
  return naam

Input achternaam
  herhaal
  Voorwaarden, mag niet: korter dan len(1) langer dan len(19), getallen bevatten, beginnen met hoofdletter (Valideren met bool), andere tekens bevatten dan ',', '-', '/'
  tot achternaam is geldig
  return naam

Input tijd
  input controleren:
  herhaal
    voorwaarden: HH:MM, met nullen, tussen 00-23 en minuten 00-59
    andere randvoorwaarde controleren:
      tussen 10 minuten en 180 minuten, tijd vooruit en zelfde dag
      klopt niet: input error





# Participant informatie verwerken
Naam samenvoegen en toevoegen aan list
Time entrie toevoegen aan list
Average time berekenen a.d.h.v. list
Boolean voor huidige participant is sneller of niet
bijhouden snelste participant

# Tussen-output
Print informatie participant
Print boolean gem. snelheid
Vraag om participant toe te voegen

# Final output
Geen nieuwe participant
  print snelste participant
  print totale participanten
  print gemiddelde





----

# ---------- Validatie (namen verplicht uit de opdracht) ----------

FUNCTION is_first_name_valid(name) -> bool
    RETURN name bestaat alleen uit letters
       AND lengte tussen 2 en 10
       AND eerste letter is hoofdletter

FUNCTION is_last_name_valid(name) -> bool
    IF lengte niet tussen 2 en 20
        RETURN False
    FOR elk teken in name
        IF teken is geen letter AND teken niet in " ,-/"
            RETURN False
    RETURN True

FUNCTION is_time_valid(time_str) -> bool
    IF lengte != 5 OR teken op positie 2 != ":"
        RETURN False
    uren = eerste 2 tekens, minuten = laatste 2 tekens
    IF uren of minuten zijn geen cijfers
        RETURN False
    RETURN uren tussen 0-23 AND minuten tussen 0-59

FUNCTION is_duration_valid(start, end) -> bool       # start/end in minuten
    RETURN 10 <= end - start <= 180                  # dekt ook "start vóór end"


# ---------- Omrekenen ----------

FUNCTION time_to_minutes(time_str) -> int            # "08:30" -> 510
    RETURN uren * 60 + minuten

FUNCTION minutes_to_hhmm(minutes) -> str             # 47 -> "00:47"
    RETURN (minutes // 60) en (minutes % 60), allebei 2 cijfers met voorloopnul


# ---------- Input-helpers: vragen tot het goed is ----------

FUNCTION ask_until_valid(prompt, check_function)
    REPEAT
        value = INPUT(prompt)
        IF NOT check_function(value)
            PRINT "Input error"
    UNTIL check_function(value)
    RETURN value

FUNCTION ask_duration() -> int
    REPEAT
        start  = time_to_minutes(ask_until_valid("Start time? ", is_time_valid))
        finish = time_to_minutes(ask_until_valid("Finish time? ", is_time_valid))
        IF NOT is_duration_valid(start, finish)
            PRINT "Input error"               # daarna opnieuw vanaf Start time
    UNTIL is_duration_valid(start, finish)
    RETURN finish - start

FUNCTION ask_new_participant() -> bool
    REPEAT
        answer = INPUT("New participant? (Yes or No): ")
        IF answer niet "Yes" en niet "No"
            PRINT "Input error"
    UNTIL answer is "Yes" OR "No"
    RETURN answer == "Yes"


# ---------- Hoofdprogramma ----------

count = 0
total_time = 0
fastest_time = 0
fastest_name = ""
doorgaan = True

WHILE doorgaan
    first = ask_until_valid("First name? ", is_first_name_valid)
    last  = ask_until_valid("Last name? ", is_last_name_valid)
    name  = first + " " + last
    duration = ask_duration()

    count = count + 1
    total_time = total_time + duration
    average = total_time / count

    IF count == 1 OR duration < fastest_time
        fastest_time = duration
        fastest_name = name

    PRINT name + " did it in " + minutes_to_hhmm(duration)
    IF duration <= average
        PRINT "This participant is currently faster than the average."
    ELSE
        PRINT "This participant is currently slower than the average."

    doorgaan = ask_new_participant()

PRINT "Fastest participant: " + fastest_name + " (" + minutes_to_hhmm(fastest_time) + ")"
PRINT "Total participants: " + count
PRINT "Average time: " + minutes_to_hhmm(total_time // count)
