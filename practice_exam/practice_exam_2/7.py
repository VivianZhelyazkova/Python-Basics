clients = int(input())
grand_total = 0
for client in range(clients):
    command = input()
    total_per_client = 0
    items = 0
    discount = 1
    while command != "Finish":
        items += 1
        if command == "basket":
            price = 1.50
            total_per_client += price
        elif command == "wreath":
            price = 3.80
            total_per_client += price
        elif command == "chocolate bunny":
            price = 7
            total_per_client += price
        command = input()
    if items % 2 == 0:
        discount = 0.80
    total_with_discount = total_per_client * discount

    grand_total += total_with_discount
    print(f"You purchased {items} items for {total_with_discount:.2f} leva.")
average = grand_total / clients
print(f"Average bill per client is: {average:.2f} leva.")
