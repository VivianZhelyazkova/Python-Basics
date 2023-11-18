month = input()
days = int(input())


studio = 0
apartment = 0
studio_discount = 1
apartment_discount = 1
months = ["May", "June", "July", "August", "September", "October"]

if month not in months:
    print("Error")

if month == "May":
    studio = 50
    apartment = 65
    if 14 >= days > 7:
        studio_discount = 0.95
        apartment_discount = 1
    if days > 14:
        studio_discount = 0.70
        apartment_discount = 0.90
if month == "October":
    studio = 50
    apartment = 65
    if 14 >= days > 7:
        studio_discount = 0.95
        apartment_discount = 1
    if days > 14:
        studio_discount = 0.70
        apartment_discount = 0.90
if month == "June":
    studio = 75.20
    apartment = 68.70
    if days > 14:
        studio_discount = 0.80
        apartment_discount = 0.90
    if days <= 14:
        studio_discount = 1
        apartment_discount = 1
if month == "September":
    studio = 75.20
    apartment = 68.70
    if days > 14:
        studio_discount = 0.80
        apartment_discount = 0.90
        if days <= 14:
            studio_discount = 1
            apartment_discount = 1
if month == "July":
    studio = 76
    apartment = 77
    if days > 14:
        studio_discount = 1
        apartment_discount = 0.90
    if days <= 14:
        studio_discount = 1
        apartment_discount = 1
if month == "August":
    studio = 76
    apartment = 77
    if days > 14:
        studio_discount = 1
        apartment_discount = 0.90
    if days <= 14:
        studio_discount = 1
        apartment_discount = 1

print(f"Apartment: {days  *  apartment * apartment_discount:.2f} lv.\n"
              f"Studio: {days  *  studio * studio_discount:.2f} lv.")