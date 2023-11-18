days = int(input())
food_total = float(input())
biscuits = 0
food_eaten = 0
total_dog_food = 0
total_cat_food = 0

for day in range(1, days + 1):
    dog_food_per_day = int(input())
    cat_food_per_day = int(input())
    if day % 3 == 0:
        biscuits += (dog_food_per_day + cat_food_per_day) * 0.10
    food_eaten += dog_food_per_day + cat_food_per_day
    total_dog_food += dog_food_per_day
    total_cat_food += cat_food_per_day
total_percent = food_eaten / food_total * 100
dog_percent = total_dog_food / food_eaten * 100
cat_percent = total_cat_food / food_eaten * 100

print(f"Total eaten biscuits: {int(biscuits)}gr.")
print(f"{total_percent:.2f}% of the food has been eaten.")
print(f"{dog_percent:.2f}% eaten from the dog.")
print(f"{cat_percent:.2f}% eaten from the cat.")