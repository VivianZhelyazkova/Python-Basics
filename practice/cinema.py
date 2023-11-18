premiere = 12
normal = 7.50
discount = 5

type = input()
rows = int(input())
cols = int(input())
price = 0
if type == "Premiere":
    price = 12
elif type == "Normal":
    price = 7.50
elif type == "Discount":
    price = 5
total_seats = rows * cols
profit = total_seats * price
print(f"{profit:.2f} leva")

