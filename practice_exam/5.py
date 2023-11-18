
fruit = input()
fruit_list = ["Watermelon", "Mango", "Pineapple", "Raspberry"]
set_size = input()
sets_ordered = int(input())

if set_size == "small":
    if fruit == "Watermelon":
        price_per_piece = 56
    elif fruit == "Mango":
        price_per_piece = 36.66
    elif fruit == "Pineapple":
        price_per_piece = 42.10
    elif fruit == "Raspberry":
        price_per_piece = 20
    price_per_set = 2 * price_per_piece
elif set_size == "big":
    if fruit == "Watermelon":
        price_per_piece = 28.70
    elif fruit == "Mango":
        price_per_piece = 19.60
    elif fruit == "Pineapple":
        price_per_piece = 24.80
    elif fruit == "Raspberry":
        price_per_piece = 15.20
    price_per_set = 5 * price_per_piece

total_price = sets_ordered * price_per_set

if 400 <= total_price <= 1000:
    discount = 0.85
elif total_price > 1000:
    discount = 0.50
else:
    discount = 1
final_price = total_price * discount
print(f"{final_price:.2f} lv.")
