day_of_the_week = input()

week_days = ["Monday", "Tuesday", "Wednesday", "Friday", "Thursday"]
weekend_days = ["Saturday", "Sunday"]
if day_of_the_week in week_days:
    print("Working day")
elif day_of_the_week in weekend_days:
    print("Weekend")
else:
    print("Error")
