# A1W3P2 - Advanced palindrome
# Description: see README.md in this folder
# Deadline: 2027-01-08 23:59 (CET)

# Inputs
user_input = input("Type a word: ")
user_input = user_input.replace(" ", "")
user_input = user_input.replace(",", "")
user_input = user_input.replace(".", "")
user_input = user_input.replace("?", "")
user_input = user_input.replace("!", "")
user_input = user_input.replace(";", "")
user_input = user_input.lower()

# Processing
# lengte woord bepalen
# eerste en laatste positie vergelijken
# door naar volgende positie

for count in range(len(user_input) // 2):
    if user_input[count] != user_input[-(count + 1)]:
        print("This is not a palindrome")
        break
else:
    print("This is a palindrome")
