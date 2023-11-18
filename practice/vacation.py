budget = float(input())
season = input()

if budget <= 1000:
    room = "Camp"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.65
    elif season == "Winter":
        place = "Morocco"
        price = budget * 0.45
elif budget <= 3000:
    room = "Hut"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.80
    elif season == "Winter":
        place = "Morocco"
        price = budget * 0.60
elif budget > 3000:
    room = "Hotel"
    if season == "Summer":
        place = "Alaska"
        price = budget * 0.90
    elif season == "Winter":
        place = "Morocco"
        price = budget * 0.90

print(f"{place} - {room} - {price:.2f}")
