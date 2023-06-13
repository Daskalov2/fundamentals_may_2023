n_snowballs = int(input())
highest = 0
highest_weight = 0
highest_time = 0
highest_quality = 0

for snowball in range(1 , n_snowballs + 1):
    weight_user = int(input())
    time_user = int(input())
    quality = int(input())
    value = (weight_user / time_user) ** quality
    if value > highest:
        highest = value
        highest_weight = weight_user
        highest_time = time_user
        highest_quality = quality

print(f"{highest_weight} : {highest_time} = {highest:.0f} ({highest_quality})")

