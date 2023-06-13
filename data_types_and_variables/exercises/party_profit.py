# from math import floor

grp_size = int(input())
days = int(input())
coins = 0

for day in range(1, days + 1):
    coins += 50
    coins -= grp_size * 2
    if day % 3 == 0:
        coins -= grp_size * 3
    if day % 5 == 0:
        coins += grp_size * 20
        if day % 5 == 0 and day % 3 == 0:
            coins -= grp_size * 2
    if day % 10 == 0:
        grp_size -= 2
    if day % 15 == 0:
        grp_size += 5

coins //= grp_size

print(f"{grp_size} companions received {coins:.0f} coins each.")
