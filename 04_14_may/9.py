days = int(input())
room = input()
grade = input()

price = 0
apartment_discount = 1
president_discount = 1
discount = 1

if room == "room for one person":
    price = 18 * (days - 1)
if room == "apartment":
    price = 25 * (days - 1)
    if days < 10:
        discount = 0.70
    if 10 <= days <= 15:
        discount = 0.65
    if days > 15:
        discount = 0.50
if room == "president apartment":
    price = 35 * (days - 1)
    if days < 10:
        discount = 0.90
    if 10 <= days <= 15:
        discount = 0.85
    if days > 15:
        discount = 0.80


total = price * discount

if grade == "positive":
    tip = total * 0.25
    print(f"{total + tip:.2f}")
if grade == "negative":
    tip = total * 0.10
    print(f"{total - tip:.2f}")





