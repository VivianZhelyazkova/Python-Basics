hours = int(input())
day = input()

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if day in working_days and 10 <= hours <= 18:
    print("open")
else:
    print("closed")