import math
tournaments = int(input())
starting_points = int(input())
# final_points = starting_points
W = 2000
F = 1200
SF = 720

points = 0
wins = 0
for _ in range(tournaments):
    stage = input()
    if stage == "W":
        points += W
        wins += 1
    elif stage == "F":
        points += F
    elif stage == "SF":
        points += SF

final_points = points + starting_points
average_points = math.floor(points / tournaments)
wins_percent = wins / tournaments * 100
print(f"Final points: {final_points}\n"
      f"Average points: {average_points}\n"
      f"{wins_percent:.2f}%")

