lines = int(input())
open_bracket = 0
closed_bracket = 0

for line in range(1, lines + 1):
    user_input = input()
    if user_input == "(":
        open_bracket += 1
    elif user_input == ")":
        closed_bracket += 1
    else:
        continue
    if closed_bracket > open_bracket:
        print("UNBALANCED")
        exit()
    if open_bracket == closed_bracket:
        continue
    if open_bracket - closed_bracket != 1:
        print("UNBALANCED")
        exit()
    if open_bracket - closed_bracket == 1:
        continue

print("BALANCED")
