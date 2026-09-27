# A1W3P5 - Multiplication table
# Description: see README.md in this folder
# Deadline: 2026-09-25 23:59 (CEST)

# Inputs nvt

# Processing en output

print("     ", end="")
for top_row_nmbr in range(1, 11):
    print(f"{top_row_nmbr:^5}", end="")
print()
for step in range(1, 11):
    print(f"{step:^5}", end="")
    for row in range(1, 11):
        print(f"{step * row:^5}", end="")
    print()

# verbetering, width toevoegen voor als je verder wilt dan 10
# kopregel print(f"{'':{width}}", end="")
# dan kan dit ook:
# for column in range(1, size + 1):
#     print(f"{column:{width}}", end="")
