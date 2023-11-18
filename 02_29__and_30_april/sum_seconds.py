from math import floor

time_first = int(input())
time_second = int(input())
time_third = int(input())

total_time = time_first + time_second + time_third

time_as_minutes = total_time // 60
time_as_seconds = total_time % 60
time_as_minutes = floor(time_as_minutes)
if time_as_seconds < 10:
    print(f"{time_as_minutes}:0{time_as_seconds}")
else:
    print(f"{time_as_minutes}:{time_as_seconds}")
