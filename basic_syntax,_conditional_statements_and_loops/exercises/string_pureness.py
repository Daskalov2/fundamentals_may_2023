number = int(input())
contains = 0

for i in range(number):
    my_string = input()
    for character in my_string:
        if character == "," or character == "." or character == "_":
            contains += 1

    if contains >= 1:
        print(f"{my_string} is not pure!")
    else:
        print(f"{my_string} is pure.")