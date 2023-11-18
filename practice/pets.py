from math import ceil, floor

days = int(input())
food_provided = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input())

food_needed = (dog_food_per_day + cat_food_per_day + turtle_food_per_day / 1000) * days

if food_provided >= food_needed:
    food_left = int(floor(food_provided - food_needed))
    print(f"{food_left} kilos of food left.")
else:
    missing_food = int(ceil(food_needed - food_provided))
    print(f"{missing_food} more kilos of food are needed.")