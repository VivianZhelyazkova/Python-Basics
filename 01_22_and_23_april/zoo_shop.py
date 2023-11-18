#dog_food_price = 2.50
#cat_food_price = 4
dog_food_quantity = int(input())
cat_food_quantity = int(input())
if 0<=dog_food_quantity<=100:
    print(str(((dog_food_quantity) * 2.50) + ((cat_food_quantity) * 4)) + " lv.")
else:
    print("error")
