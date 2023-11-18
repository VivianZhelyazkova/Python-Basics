goal = 10000
total_steps = 0
command = ""

while total_steps < goal:
    steps = int(input())
    total_steps += steps
    if total_steps >= goal:
        diff = total_steps - goal
        print(f"Goal reached! Good job!\n{diff} steps over the goal!")
        break
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        total_steps += steps_to_home
        if total_steps < goal:
            diff = goal - total_steps
            print(f"{diff} more steps to reach goal.")
        break
