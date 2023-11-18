from unicodedata import category

vip_price = 499.99
normal_price = 249.99

budget = float(input())
category = input()
group_count = int(input())
if category == "VIP":
    price = vip_price
elif category == "Normal":
    price = normal_price
if 1 <= group_count <= 4:
    transport = 0.75
elif 5 <= group_count <= 9:
    transport = 0.60
elif 10 <= group_count <= 24:
    transport = 0.50
elif 25 <= group_count <= 49:
    transport = 0.40
else:
    transport = 0.25

ticket_total = group_count * price
transport_total = budget * transport
total_cost = ticket_total + transport_total
budget_left = abs(total_cost - budget)
if budget >= total_cost:
    print(f"Yes! You have {budget_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {budget_left:.2f} leva.")