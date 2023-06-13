first_positive_number = int(input())
second_positive_number = int(input())
greatest_number = 0

for i in range(1, second_positive_number + 1):
    if i % first_positive_number == 0 and i <= second_positive_number:
        greatest_number = i

print(greatest_number)
