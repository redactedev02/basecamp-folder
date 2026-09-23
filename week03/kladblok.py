# A1W3P1 - Simple palindrome
# Description: see README.md in this folder
# Deadline: 2027-01-08 23:59 (CET)

# Inputs
user_input = input("Type a word: ")

# Processing
# lengte woord bepalen
# eerste en laatste positie vergelijken
# door naar volgende positie
length = len(user_input)
input_split = length // 2
loop_times = 1
start_progress = 0
end_progress = 1

for count in range(input_split):
    if loop_times == input_split:
        print("This is a palindrome")
        break
    elif user_input[start_progress] == user_input[-end_progress]:
        start_progress += 1
        end_progress += 1
        loop_times += 1
    else:
        print("This is not a palindrome")
        break

# Outputs
b
