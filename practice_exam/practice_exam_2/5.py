import sys

hat_trick = False
command = input()
max_num = -sys.maxsize
best_player = ""

while command != "END":
    goals = int(input())

    if goals > max_num:
        max_num = goals
        best_player = command

    if goals >= 3:
        hat_trick = True

    if goals >= 10:
        break

    command = input()

if hat_trick:
    print(f"{best_player} is the best player!\n"
          f"He has scored {max_num} goals and made a hat-trick !!!")
else:
    print(f"{best_player} is the best player!\n"
          f"He has scored {max_num} goals.")
