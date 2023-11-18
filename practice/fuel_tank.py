fuel_type = input()
liters = int(input())
fuel_list = ["Diesel", "Gasoline", "Gas"]
if fuel_type not in fuel_list:
    print("Invalid fuel!")
else:
    if liters >= 25:
        if fuel_type == "Diesel":
            fuel = "diesel"
        elif fuel_type == "Gasoline":
            fuel = "gasoline"
        elif fuel_type == "Gas":
            fuel = "gas"
        print(f"You have enough {fuel}.")
    else:
        if fuel_type == "Diesel":
            fuel = "diesel"
        elif fuel_type == "Gasoline":
            fuel = "gasoline"
        elif fuel_type == "Gas":
            fuel = "gas"
        print(f"Fill your tank with {fuel}!")

