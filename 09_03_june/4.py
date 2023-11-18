
start = int(input())
final = int(input())
magic_number = int(input())
found = False
combination = 0

for first_number in range(start, final + 1):
    for second_number in range(start, final + 1):
        combination += 1
        if first_number + second_number == magic_number:
            found = True
            break
    if found:
        break
if found:
    print(f"Combination N:{combination} ({first_number} + {second_number} = {magic_number})")
if not found:
    print(f"{combination} combinations - neither equals {magic_number}")