first_string = input()
second_string = input()
last_printed_string = ""


for index_character in range(len(first_string)):
    left_part = second_string[:index_character + 1]
    right_part = first_string[index_character + 1:]
    new_string = (left_part + right_part)
    if new_string == last_printed_string:
        continue
    last_printed_string = new_string
    if last_printed_string == first_string:
        continue
    print(last_printed_string)
 