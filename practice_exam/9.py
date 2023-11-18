capacity = float(input())
command = input()
bag_count = 0
while command != "End":
    bag_volume = float(command)
    if capacity < bag_volume:
        print(f"No more space!")
        break
    bag_count += 1
    if bag_count % 3 == 0:
        bag_volume = bag_volume + bag_volume * 0.10
    capacity -= bag_volume
    command = input()
    if command == "End":
        break
    bag_volume = float(command)

if command == "End":
    print(f"Congratulations! All suitcases are loaded!")
print(f"Statistic: {bag_count} suitcases loaded.")

