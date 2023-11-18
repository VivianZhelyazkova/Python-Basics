from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
meter_per_second = float(input())

time_needed = distance_in_meters * meter_per_second
slow_down = (floor(distance_in_meters / 50)) * 30
his_time = time_needed + slow_down

if his_time < record_in_seconds:
    print(f" Yes! The new record is {his_time:.2f} seconds.")
else:
    slower = his_time - record_in_seconds
    print(f" No! He was {slower:.2f} seconds slower.")



