# input

budget = int(input())
total_price = 0

while True:
    user_input = input()
    if user_input == "End":
        print(f"You bought everything needed.")
        break
    elif user_input != "End":
        user_input = float(user_input)
    total_price += user_input
    if total_price > budget:
        print(f"You went in overdraft!")
        break