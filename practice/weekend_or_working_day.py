day = input()
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend_days = ["Sunday", "Saturday"]

if day in working_days:
    print("Working day")
elif day in weekend_days:
    print("Weekend")
else:
    print("Error")