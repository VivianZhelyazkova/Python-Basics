goal =  10000

command = input()
total_steps = 0

while command != "Going home":
    current_steps = int(command)
    total_steps += current_steps
    if total_steps >= goal:
        overkill = total_steps - goal
        print(f"Goal reached! Good job!\n"
              f"{overkill} steps over the goal!")
        break
    command = input()
else:
    steps_to_home = int(input())
    total_steps += steps_to_home
    overkill = abs(total_steps - goal)
    if total_steps >= goal:
        print(f"Goal reached! Good job!\n"
              f"{overkill} steps over the goal!")
    if total_steps < goal:
        print(f"{overkill} more steps to reach goal.")