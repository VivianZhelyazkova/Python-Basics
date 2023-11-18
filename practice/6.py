months = int(input())
water = 0
electricity = 0
internet = 0
others = 0
e = 0

for _ in range(1, months + 1):
    electricity = float(input())
    e += electricity
    water += 20
    internet += 15
    others = (e + water + internet) + ((e + water + internet) * 0.2)

total_electricity = e
total_water = months * 20
total_internet = months * 15

# others = (electricity + total_water + total_internet) + ((electricity + total_water + total_internet) * 0.20)
total = total_electricity + total_water + total_internet + others
average = total / months

print(f"Electricity: {total_electricity:.2f} lv\n"
      f"Water: {total_water:.2f} lv\n"
      f"Internet: {total_internet:.2f} lv\n"
      f"Other: {others:.2f} lv\n"
      f"Average: {average:.2f} lv")

