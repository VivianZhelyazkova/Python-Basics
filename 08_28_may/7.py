width = int(input())
length = int(input())
height = int(input())
apartment_volume = width * length * height
box = 1
boxes_volume = 0

command = input()

while command != "Done":
    boxes = int(command)
    boxes_volume += boxes
    if boxes_volume > apartment_volume:
        print(f"No more free space! You need {boxes_volume - apartment_volume}"
              f" Cubic meters more.")
        break
    command = input()
else:
    print(f"{apartment_volume - boxes_volume} Cubic meters left.")