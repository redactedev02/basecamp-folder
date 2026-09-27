# A1W3A2 - Mountain climbing time trail
# Description: see README.md in this folder
# Deadline: 2026-09-25 23:59 (CEST)

# Functies voor validatie van input
def is_first_name_valid(name):
    return (
        name.isalpha()
        and len(name) >= 2
        and len(name) <= 10
        and name[0].isupper()
    )

# omgekeerd, dus geen else, hele reeks door!
def is_special_char_valid(last_name):
        for character in last_name:
            if not character.isalpha() and character not in " ,-/":
                return False
        return True

def is_last_name_valid(last_name):
    if (
         len(last_name) >= 2
         and len(last_name) <= 20
         and is_special_char_valid
    ):
        return True
    else: return False

def is_time_valid(time_str):
     if (
         time_str[2] in ":;."
         and time_str[0:2].isdigit()
         and time_str[3:5].isdigit()
         and int(time_str[0:2]) <= 23
         and int(time_str[3:5]) <= 59
         and len(time_str) == 5
     ):
          return True
     else: return False

def time_to_minutes(time_str):
        return int(time_str[0:2]) * 60 + int(time_str[3:5])

def is_duration_valid(start_time, finish_time):
    return finish_time - start_time >= 10 and finish_time - start_time <= 180

# Processing
def update_record(new_time):


# Outputs
