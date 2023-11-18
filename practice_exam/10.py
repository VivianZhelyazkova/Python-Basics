days = int(input())
winner = 0
loser = 0
total_money = 0
for _ in range(days):
    command = input()
    charity = 0
    wins = 0
    loses = 0
    while command != "Finish":
        result = input()
        if result == "win":
            wins += 1
            charity += 20
        elif result == "lose":
            loses += 1
        command = input()
    if wins > loses:
        winner += 1
        charity = charity + charity * 0.10
    elif loses > wins:
        loser += 1
    total_money += charity


if winner > loser:
    total_money = total_money + total_money * 0.20
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")