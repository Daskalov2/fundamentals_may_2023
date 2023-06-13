lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expenses = 0

broken_helmets = 0
broken_swords = 0
broken_shields = 0
broken_armors = 0


for fight_lost in range(1, lost_fights + 1):
    if fight_lost % 2 == 0:
        broken_helmets += 1
    if fight_lost % 3 == 0:
        broken_swords += 1
    if fight_lost % 3 == 0 and fight_lost % 2 == 0:
        broken_shields += 1
        if broken_shields % 2 == 0:
            broken_armors += 1

total_expenses = broken_helmets * helmet_price + broken_swords * sword_price + broken_shields * \
                 shield_price + broken_armors * armor_price

print(f"Gladiator expenses: {total_expenses:.2f} aureus")

