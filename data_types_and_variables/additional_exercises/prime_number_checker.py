number = int(input())
true = 0
false = 0

if number > 1:
    for i in range(2, number):
        if number % i == 0:
            false += 1
        else:
            true += 1

if false == 0:
    print("True")
else:
    print("False")