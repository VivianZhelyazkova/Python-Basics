floors = int(input())
rooms = int(input())
letter = ""
for current_floor in range(floors, 0, -1):
    if current_floor == floors:
        letter = "L"
    elif current_floor % 2 != 0:
        letter = "O"
    elif current_floor % 2 == 0:
        letter = "A"
    for room in range(rooms):
        print(f"{letter}{current_floor}{room}" ,end = ' ')
    print()

