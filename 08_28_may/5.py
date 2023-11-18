change = float(input())
change_as_coins = int(change * 100)
coins_count = 0
while change_as_coins > 0:
    if change_as_coins >= 200:
        change_as_coins -= 200
    elif change_as_coins >= 100:
        change_as_coins -= 100
    elif change_as_coins >= 50:
        change_as_coins -= 50
    elif change_as_coins >= 20:
        change_as_coins -= 20
    elif change_as_coins >= 10:
        change_as_coins -= 10
    elif change_as_coins >= 5:
        change_as_coins -= 5
    elif change_as_coins >= 2:
        change_as_coins -= 2
    elif change_as_coins == 1:
        change_as_coins -= 1
    coins_count += 1

else:
    print(coins_count)

