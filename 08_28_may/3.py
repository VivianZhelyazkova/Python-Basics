trip_cost = float(input())
available_money = float(input())

still_need_money = True
command = ""
spend_count = 0
day_count = 0

while still_need_money:
    command = input()
    money = float(input())
    day_count += 1
    if command == "spend":
        available_money -= money
        if money > available_money:
            available_money = 0
        spend_count += 1
        if spend_count >= 5:
            print(f"You can't save the money.\n"
                  f"{day_count}")
            break
    if command == "save":
        available_money += money
    if available_money >= trip_cost:
        print(f"You saved the money for {day_count} days.")
        still_need_money = False
