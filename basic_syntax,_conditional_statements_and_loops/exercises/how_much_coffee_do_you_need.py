needed_coffee = 0

while True:
    user_input = input()
    if user_input == "END":
        break
    elif user_input == "coding" or user_input == "dog" or user_input == "cat" or user_input == "movie":
        needed_coffee += 1
    elif  user_input == "CODING" or user_input == "DOG" or user_input == "CAT" or user_input == "MOVIE":
        needed_coffee += 2
    else:
        continue

if needed_coffee > 5:
    print("You need extra sleep")
else:
    print(f"{needed_coffee}")
