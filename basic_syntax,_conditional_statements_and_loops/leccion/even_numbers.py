# input

nums = int(input())

# logic

for i in range(nums):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        break
    elif number % 2 == 0:
        if nums - i == 1:
            print("All numbers are even.")
        else:
            continue
