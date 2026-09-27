# A1W3P3 - Modular rectangles
# Description: see README.md in this folder

# Input
width = int(input("Enter a width: "))
height = int(input("Enter a height: "))
count = 0


# Processing
# Tellen tot en met 9, dan weer naar 0
def counter(count):
    count = (count + 1) % 10
    return count


# printen getal / output
for row_count in range(height):
    for length_count in range(width):
        print(f"{count} ", end="")
        count = counter(count)
    print()


# onnodig if-else. else is gelijk aan het einde van de for loop. Aangezien aan het einde een enter moet kunnen we gewoon buiten de for loop print() zetten.
# for length_count in range(width):
#     if length_count == (width - 1):
#         print(f"{count} ")
#     else:
#         print(f"{count} ", end="")
#     count = counter(count)
