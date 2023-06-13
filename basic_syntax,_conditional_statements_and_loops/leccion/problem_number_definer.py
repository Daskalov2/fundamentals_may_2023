# input
number = float(input())
result = ""
# logic
if number == 0:
    result = "zero"
elif 0 < number < 1:
    result = "small positive"
elif 1 <= number <= 1000000:
    result = "positive"
elif number > 1000000:
    result = "large positive"
elif -1 < number < 0:
    result = "small negative"
elif -1000000 <= number <= -1 :
    result = "negative"
elif number < -1000000:
    result = "large negative"

# output
print(result)
