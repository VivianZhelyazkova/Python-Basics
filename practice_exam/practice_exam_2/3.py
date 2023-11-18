
isolation_count = int(input())
isolation_type = input()
delivery_method = input()

price_per_piece = 0
discount = 0
if isolation_count < 10:
    print("Invalid order")
else:
    if isolation_type == "90X130":
        price_per_piece = 110
        if 60 > isolation_count > 30:
            discount = 0.95
        elif isolation_count > 60:
            discount = 0.92
        else:
            discount = 1
    elif isolation_type == "100X150":
        price_per_piece = 140
        if 80 > isolation_count > 40:
            discount = 0.94
        elif isolation_count > 80:
            discount = 0.90
        else:
            discount = 1
    elif isolation_type == "130X180":
        price_per_piece = 190
        if 50 > isolation_count > 20:
            discount = 0.93
        elif isolation_count > 50:
            discount = 0.88
        else:
            discount = 1
    elif isolation_type == "200X300":
        price_per_piece = 250
        if 50 > isolation_count > 25:
            discount = 0.91
        elif isolation_count > 50:
            discount = 0.86
        else:
            discount = 1
    if delivery_method == "With delivery":
        delivery_price = 60
    else:
        delivery_price = 0
    total_price = price_per_piece * isolation_count * discount + delivery_price
    if isolation_count > 99:
        second_discount = 0.96
    else:
        second_discount = 1
    final = total_price * second_discount
    print(f"{final:.2f} BGN")
