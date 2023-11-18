goal = int(input())
command = input()
total = 0
price = 0
while command != "closed":
    if command == "haircut":
        style = input()
        if style == "mens":
            price = 15
        elif style == "ladies":
            price = 20
        elif style == "kids":
            price = 10
    if command == "color":
        style = input()
        if style == "touch up":
            price = 20
        elif style == "full color":
            price = 30
    total += price
    if command == "closed":
        break
    if total >= goal:
        break
    command = input()
if total >= goal:
    print(f"You have reached your target for the day!")
else:
    less = goal - total
    print(f"Target not reached! You need {int(less)}lv. more.")
print(f"Earned money: {int(total)}lv.")