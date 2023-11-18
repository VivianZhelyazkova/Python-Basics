kilometers = int(input())
time = input()
starting_price = 0

if kilometers < 20:
    starting_price = 0.70
    day_tariff = 0.79
    night_tariff = 0.90
elif kilometers < 100:
    day_tariff = 0.09
    night_tariff = 0.09
else:
    day_tariff = 0.06
    night_tariff = 0.06
if time == "day":
    tariff = day_tariff
elif time == "night":
    tariff = night_tariff
total = starting_price + kilometers * tariff
print(f"{total:.2f}")