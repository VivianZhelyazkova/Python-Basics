month = input()
nights = int(input())
studio = 0
apartment = 0

if month == "May" or month == "October":
    studio = 50
    if 14 > nights > 7:
        studio *= 0.95
    elif 7 < nights > 14:
        studio *= 0.70
    apartment = 65
elif month == "June" or month == "September":
    studio = 75.20
    if nights > 14:
        studio *= 0.80
    apartment = 68.70
elif month == "July" or month == "August":
    studio = 76
    apartment = 77
if nights > 14:
    apartment *= 0.90
total_studio = nights * studio
total_apartment = nights * apartment

print(f"Apartment: {total_apartment:.2f} lv.\n"
      f"Studio: {total_studio:.2f} lv.")