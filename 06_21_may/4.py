age = int(input())
washing_machine = float(input())
toy_price = int(input())
money = 0
toys = 0

for bd in range (1,age +1):
    if bd % 2 == 0:
        money += bd * 5
        money -= 1
    elif bd % 2 != 0:
        toys += 1

toys_cost = toys * toy_price
total = toys_cost + money
money_left = abs(total - washing_machine)
if total >= washing_machine:
    print(f"Yes! {money_left:.2f}")
else:
    print(f"No! {money_left:.2f}")
