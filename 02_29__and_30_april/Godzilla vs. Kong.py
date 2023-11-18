budget = float(input())
extras_count = int(input())
extras_outfit_price = float(input())

decor = budget * 0.10
cost_for_extras = extras_count * extras_outfit_price

if extras_count > 150:
    extras_outfit_price = extras_outfit_price * 0.90
    cost_for_extras = extras_count * extras_outfit_price

total = cost_for_extras + decor

if budget < total:
    print(f"Not enough money! \nWingard needs {total - budget:.2f} leva more.")
if total <= budget:
    print(f"Action!\nWingard starts filming with {budget - total:.2f} leva left.")
