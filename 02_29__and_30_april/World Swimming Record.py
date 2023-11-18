
world_record = float(input())
distance_in_meters = float(input())
seconds_needed_for_meter = float(input())

time_needed = distance_in_meters * seconds_needed_for_meter
slow_down = distance_in_meters // 15 * 12.5
total_time = time_needed + slow_down

if total_time < world_record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - world_record:.2f} seconds slower.")

