destination = input()
minimum_budget = float(input())
current_budget = 0

while destination != "End":
    add_to_budget = float(input())
    current_budget += add_to_budget
    if current_budget >= minimum_budget:
        print(f"Going to {destination}!")
        current_budget = 0
        destination = input()
        if destination == "End":
            break
        minimum_budget = float(input())
