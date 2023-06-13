n = int(input())

for first_loop in range(0, n):
    for second_loop in range(0, n):
        for third_loop in range(0, n):
            print(f"{chr(97 + first_loop)}{chr(97 + second_loop)}{chr(97 + third_loop)}")
