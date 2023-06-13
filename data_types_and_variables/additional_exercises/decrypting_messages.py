key = int(input())
lines = int(input())
message = ""

for line in range(1, lines + 1):
    letter = input()
    message = ord(letter)
    message += key
    message = chr(message)
    print(message, end="")
