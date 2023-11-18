minutes_per_day = int(input())
walks_per_day = int(input())
calories_per_day = int(input())

total_minutes = walks_per_day * minutes_per_day
total_calories = total_minutes * 5
needed_percent = calories_per_day / 2

if total_calories >= needed_percent:
    print(f"Yes, the walk for your cat is enough."
        f" Burned calories per day: {total_calories}.")
else:
    print(f"No, the walk for your cat is not enough."
    f" Burned calories per day: {total_calories}.")