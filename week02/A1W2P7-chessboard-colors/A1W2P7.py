# A1W2P7 - Chessboard colors
# Description: see README.md in this folder
# Deadline: 2026-09-18 23:59 (CEST)

# Inputs
position = input("Enter a position: ").upper()
color = "Erorrrrrr"

# validatie van input
valid = False
while not valid:
    if position[0] in "ABCDEFGH" and position[1] in "12345678" and len(position) == 2:
        break
    else:
        position = input("Enter a valid position: ")


# Processing the color
starts_black = position[0] in "ACEG"
if starts_black and int(position[1]) % 2 == 0:
    color = "White"
if starts_black and int(position[1]) % 2 == 1:
    color = "Black"
if not starts_black and int(position[1]) % 2 == 0:
    color = "Black"
if not starts_black and int(position[1]) % 2 == 1:
    color = "White"


# output
print(color)
