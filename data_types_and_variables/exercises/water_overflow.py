number_of_lines = int(input())
capacity = 255
total_water = 0

for i in range(number_of_lines):
    user_water = int(input())
    total_water += user_water
    if total_water > capacity:
        total_water -= user_water
        print("Insufficient capacity!")
        continue

print(total_water)