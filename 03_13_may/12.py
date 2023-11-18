town = input()
sales = float(input())

commission = 0
town_list = ["Sofia", "Varna", "Plovdiv"]


if town == "Sofia":
    if 0 <= sales <= 500:
        commission = 0.05
    elif 500 <= sales <= 1000:
        commission = 0.07
    elif 1000 <= sales <= 10000:
        commission = 0.08
    elif sales > 1000:
        commission = 0.12

if town == "Varna":
    if 0 <= sales <= 500:
        commission = 0.045
    elif 500 <= sales <= 1000:
        commission = 0.075
    elif 1000 <= sales <= 10000:
        commission = 0.10
    elif sales > 1000:
        commission = 0.13

if town == "Plovdiv":
    if 0 <= sales <= 500:
        commission = 0.055
    elif 500 <= sales <= 1000:
        commission = 0.08
    elif 1000 <= sales <= 10000:
        commission = 0.12
    elif sales > 1000:
        commission = 0.145

commission_total = sales * commission

if town in town_list and sales > 0:
    print(f"{commission_total:.2f}")
else:
    print("error")