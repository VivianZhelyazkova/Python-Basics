inheritance = float(input())
age_to_live = int(input())

money_spend = 0

for current_age in range(1800,age_to_live + 1):
    if current_age % 2 == 0:
        money_spend += 12000
    else:
        money_spend += 12000 + (50 * (current_age - 1782))

money_left = abs(inheritance - money_spend)

if inheritance >= money_spend:
    print(f"Yes! He will live a carefree life and will have {money_left:.2f} dollars left.")
else:
    print(f"He will need {money_left:.2f} dollars to survive." )