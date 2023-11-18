fruit = input()
day = input()
quantity = float(input())

banana = 0
apple = 0
orange =0
grapefruit = 0
kiwi = 0
pineapple = 0
grapes = 0

price = 0
week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
fruits = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]
if day in week_days:
    if fruit == "banana":
        price = 2.50
    elif fruit == "apple":
        price = 1.20
    elif fruit == "orange":
        price = 0.85
    elif fruit == "grapefruit":
        price = 1.45
    elif fruit == "kiwi":
        price = 2.70
    elif fruit == "pineapple":
        price = 5.50
    elif fruit == "grapes":
        price = 3.85

if day in weekend:
    if fruit == "banana":
        price = 2.70
    elif fruit == "apple":
        price = 1.25
    elif fruit == "orange":
        price = 0.90
    elif fruit == "grapefruit":
        price = 1.60
    elif fruit == "kiwi":
        price = 3.00
    elif fruit == "pineapple":
        price = 5.60
    elif fruit == "grapes":
        price = 4.20
total = price * quantity

if day not in week_days and day not in weekend or fruit not in fruits:
    print("error")
else:
    print(f"{total:.2f}")


