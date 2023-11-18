money_needed = float(input())
available_money = float(input())
days = 0
spend = 0

while available_money < money_needed and spend < 5:
    command = input()
    money = float(input())
    days += 1
    if command == "save":
        available_money += money
        spend = 0
    elif command == "spend":
        available_money -= money
        spend += 1
        if available_money < 0:
            available_money = 0

if spend == 5:
    print(f"You can't save the money.\n"
              f"{days}")
if available_money >= money_needed:
    print(f"You saved the money for {days} days.")
