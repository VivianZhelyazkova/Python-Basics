
fuel_type = input()
liters = float(input())
club_card = input()
discount = 1

if fuel_type == "Gasoline":
    price =  2.22
    if club_card == "Yes":
        price = price - 0.18
elif fuel_type == "Diesel":
    price =  2.33
    if club_card == "Yes":
        price = price - 0.12
elif fuel_type == "Gas":
    price =  0.93
    if club_card == "Yes":
        price = price - 0.08

total_price = liters * price

if 20 <= liters <= 25:
    discount = 0.92
    final_price = total_price * discount
    print(f"{final_price:.2f} lv.")
elif liters > 25:
    discount = 0.90
    final_price = total_price * discount
    print(f"{final_price:.2f} lv.")
else:
    print(f"{total_price:.2f} lv.")
