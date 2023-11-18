budget = int(input())
season = input()
fishermen = int(input())

boat_rent = 0
discount = 0
second_discount = 1
seasons_with_discount = ["Spring" , "Summer" , "Winter"]
if season == "Spring":
    boat_rent = 3000
elif season == "Autumn":
    boat_rent = 4200
elif season == "Summer":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if fishermen <= 6:
    discount = 0.90
elif 7 <= fishermen < 12:
    discount = 0.85
else:
    discount = 0.75

if fishermen % 2 == 0 and season in seasons_with_discount:
    second_discount = 0.95
else:
    second_discount = 1

total_cost = boat_rent * discount * second_discount

if budget >= total_cost:
    print(f"Yes! You have {budget - total_cost:.2f} leva left.")

if budget < total_cost:
    print(f"Not enough money! You need {total_cost - budget:.2f} leva.")

