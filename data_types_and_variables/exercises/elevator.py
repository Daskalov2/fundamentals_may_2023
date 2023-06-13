number_people = int(input())
capacity_people = int(input())
course = 1

while True:
    number_people -= capacity_people
    course += 1
    if number_people > capacity_people:
        continue
    else:
        break

print(course)