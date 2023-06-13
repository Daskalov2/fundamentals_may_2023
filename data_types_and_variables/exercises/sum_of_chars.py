n = int(input())
total_sum = 0

for lines in range(n):
    character_input = input()
    character_input = ord(character_input)
    total_sum += character_input

print(f"The sum equals: {total_sum}")