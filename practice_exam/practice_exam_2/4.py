from math import floor
total_balls = int(input())
points = 0
red = 0
orange = 0
yellow = 0
white = 0
black = 0
other = 0
for ball in range(total_balls):
    current_ball = input()
    if current_ball == "red":
        points += 5
        red += 1
    elif current_ball == "orange":
        points += 10
        orange += 1
    elif current_ball == "yellow":
        points += 15
        yellow += 1
    elif current_ball == "white":
        points += 20
        white += 1
    elif current_ball == "black":
        points = floor(int(points / 2))
        black += 1
    else:
        other += 1
        continue

print(f"Total points: {points}\n"
      f"Red balls: {red}\n"
      f"Orange balls: {orange}\n"
      f"Yellow balls: {yellow}\n"
      f"White balls: {white}\n"
      f"Other colors picked: {other}\n"
      f"Divides from black balls: {black}")