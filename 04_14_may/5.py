budget = float(input())
season = input()

destination = 0
sleep_in = 0
price = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        sleep_in = "Camp"
        price = budget * 0.30
    elif season == "winter":
        sleep_in = "Hotel"
        price = budget * 0.70

if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        sleep_in = "Camp"
        price = budget * 0.40
    elif season == "winter":
        sleep_in = "Hotel"
        price = budget * 0.80

if budget > 1000:
    destination = "Europe"
    sleep_in = "Hotel"
    price = budget * 0.90

print(f"Somewhere in {destination} \n"
      f"{sleep_in} - {price:.2f}")
