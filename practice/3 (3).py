
dancers_count = int(input())
points = float(input())
season = input()
place = input()
prize = 0
expenses = 0
if place == "Bulgaria":
    prize = dancers_count * points
    if season == "summer":
        expenses = 0.05
    elif season == "winter":
        expenses = 0.08
elif place == "Abroad":
    prize = (dancers_count * points) * 1.5
    if season == "summer":
        expenses = 0.10
    elif season == "winter":
        expenses = 0.15
total = prize - (prize * expenses)
charity = total * 0.75
left = total - charity
per_dancer = left / dancers_count

print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {per_dancer:.2f}")