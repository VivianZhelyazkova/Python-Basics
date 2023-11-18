screening_type = input()
rows = int(input())
columns = int(input())

seats = rows * columns
ticket_price = 0

if screening_type == "Premiere":
    ticket_price = 12.00
if screening_type == "Normal":
    ticket_price = 7.50
if screening_type == "Discount":
    ticket_price = 5.00

income = ticket_price * seats

print(f"{income:.2f} leva")

