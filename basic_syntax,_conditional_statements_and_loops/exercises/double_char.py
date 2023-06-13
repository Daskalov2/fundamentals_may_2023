new_string = ""
my_string = input()

while my_string != "End":
    if my_string == "Softuni":
        new_string = ""
        continue
    for character in my_string:
        new_string += character * 2
    print(new_string, end="")
    print()
    new_string = ""
    my_string = input()