
food_bought = int(input())
command = input()
total_food = 0
food_bought = food_bought * 1000
while command != "Adopted":
    food_eaten_per_day = int(command)
    total_food += food_eaten_per_day
    command = input()
    if food_bought < 0:
        break
if total_food > food_bought:
    more_food = total_food - food_bought
    print(f"Food is not enough. You need {more_food} grams more.")
if total_food <= food_bought:
    leftovers = food_bought - total_food
    print(f"Food is enough! Leftovers: {leftovers} grams.")
