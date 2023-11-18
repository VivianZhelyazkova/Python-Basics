goal = 10000


total_steps = 0
diff = 0
steps = 0
command = ""
steps_to_home = 0

while steps < goal:
    steps = int(input())
    command = input()
    total_steps += steps
    if total_steps >= goal:

        diff = abs(total_steps - goal)
        print(f"Goal reached! Good job!\n"
              f"{diff} steps over the goal!")
        break
if command == "Going home":
    steps_to_home = int(input())
    print(f"{goal - steps_to_home} more steps to reach goal.")

