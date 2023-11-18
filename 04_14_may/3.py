flowers_type = input()
flowers_count = int(input())
budget = int(input())
flowers = ["Roses", "Dahlias", "Tulips", "Narcissus", "Gladiolus"]
total_cost = 0

if flowers_count > 80 and flowers_type == "Roses":
    total_cost = (flowers_count * 5) * (1 - 0.10)
elif flowers_count <= 80 and flowers_type == "Roses":
    total_cost = flowers_count * 5
if flowers_count > 90 and flowers_type == "Dahlias":
    total_cost = (flowers_count * 3.80) * (1 - 0.15)
elif flowers_count <= 90 and flowers_type == "Dahlias":
    total_cost = flowers_count * 3.80
if flowers_count > 80 and flowers_type == "Tulips":
    total_cost = (flowers_count * 2.80) * (1 - 0.15)
elif flowers_count <= 80 and flowers_type == "Tulips":
    total_cost = flowers_count * 2.80
if flowers_count < 120 and flowers_type == "Narcissus":
    total_cost = (flowers_count * 3.00) * 1.15
elif flowers_count >= 120 and flowers_type == "Narcissus":
    total_cost = flowers_count * 3.00
if flowers_count < 80 and flowers_type == "Gladiolus":
    total_cost = (flowers_count * 2.50) * 1.20
elif flowers_count >= 80 and flowers_type == "Gladiolus":
    total_cost = flowers_count * 2.50

if flowers_type not in flowers:
    print("Error")

if total_cost <= budget and flowers_type in flowers:
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {budget - total_cost:.2f} leva left.")

if total_cost > budget and flowers_type in flowers:
    print(f"Not enough money, you need {total_cost - budget:.2f} leva more.")



