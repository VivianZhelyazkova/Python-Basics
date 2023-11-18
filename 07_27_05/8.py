name = input()
fails = 0
total = 0
current_class = 1

while current_class <= 12:
    grade = float(input())
    if grade < 4:
        fails += 1
        if fails > 1:
            break
        continue
    current_class += 1
    total += grade


if current_class <= 12:
    print(f"{name} has been excluded at {current_class} grade")
else:
    average = total / 12
    print(f"{name} graduated. Average grade: {average:.2f}")