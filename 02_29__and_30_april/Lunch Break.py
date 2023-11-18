from math import ceil

series_name = input()
episode_time = int(input())
break_time = int(input())

lunch_time = break_time / 8
chill_time = break_time / 4

total_time_needed = (lunch_time + chill_time)
time_left = (break_time - total_time_needed)

if break_time not in range(10, 120) or episode_time not in range(10, 90):
    print("Error")
else:
    if time_left >= episode_time:
        print(f"You have enough time to watch {series_name} and left"
          f" with {ceil(break_time - total_time_needed - episode_time)} minutes free time.")

    if time_left < episode_time:
        print(f"You don't have enough time to watch {series_name}, "
          f"you need {ceil(total_time_needed + episode_time - break_time)} more minutes.")
