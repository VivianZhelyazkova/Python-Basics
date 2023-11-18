month = input()
days = int(input())

studio = 0
apartment = 0

discount_studio = 0
discount_apartment = 0

if month == "May" or "October":
    studio = 50
    apartment = 65
elif 14 >= days > 7:
        discount_studio = 0.95
        print(f"Apartment: {days  *  apartment:.2f} lv.\n"
              f"Studio: {days  *  studio * discount_studio:.2f} lv.")
elif days > 14:
        discount_studio = 0.70
        discount_apartment = 0.90
        print(f"Apartment: {days  *  apartment * discount_apartment:.2f} lv.\n"
              f"Studio: {days  *  studio * discount_studio:.2f}")

if month == "June" or "September":
    studio = 75.20
    apartment = 68.70
elif days > 14:
        discount_studio = 0.80
        discount_apartment = 0.90
        print(f"Apartment: {days  *  apartment * discount_apartment:.2f} lv.\n"
              f"Studio: {days  *  studio * discount_studio:.2f} lv.")
elif days <= 14:
        print(f"Apartment: {days  *  apartment:.2f} lv.\n"
              f"Studio: {days  *  studio:.2f} lv.")

if month == "July" or "August":
    studio = 76
    apartment = 77
elif days > 14:
        discount_apartment = 0.90
        print(f"Apartment: {days  *  apartment * discount_apartment:.2f} lv.\n"
              f"Studio: {days  *  studio:.2f} lv.")
elif days <= 14:
        print(f"Apartment: {days  *  apartment:.2f} lv.\n"
              f"Studio: {days  *  studio:.2f} lv.")
