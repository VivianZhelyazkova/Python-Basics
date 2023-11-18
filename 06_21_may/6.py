actor_name = input()
academy_points = float(input())
jury_count = int(input())

total_points = academy_points

for _ in range(jury_count):
    jury_name = input()
    jury_points = float(input())
    total_points += len(jury_name) * jury_points / 2
    if total_points > 1250.5:
        break

if total_points > 1250.5:
    print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")

else:
    points_needed = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {points_needed:.1f} more!")

