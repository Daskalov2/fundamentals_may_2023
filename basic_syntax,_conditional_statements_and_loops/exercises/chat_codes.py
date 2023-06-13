number_of_messages = int(input())
message = ""

for i in range(number_of_messages):
    user_number = int(input())
    if user_number == 88:
        message = "Hello"
    elif user_number == 86:
        message = "How are you?"
    elif user_number < 88:
        message = "GREAT!"
    else:
        message = "Bye."
    print(f"{message}")
