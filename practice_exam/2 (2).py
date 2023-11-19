bag_over_20_price = float(input())
bag_in_kilos = float(input())
days = int(input())
bags_count = int(input())

if bag_in_kilos < 10:
    price = bag_over_20_price * 0.20
elif bag_in_kilos <= 20:
    price = bag_over_20_price * 0.50
else:
    price = bag_over_20_price

if days < 7:
    price *= 1.40
elif days <= 30:
    price *= 1.15
else:
    price *= 1.10
total = price * bags_count
print(f"The total price of bags is: {total:.2f} lv.")