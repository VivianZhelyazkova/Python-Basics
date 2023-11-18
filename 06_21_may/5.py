tabs_count = int(input())
salary = float(input())

FACEBOOK = 150
INSTAGRAM = 100
REDDIT = 50
# fine = 0

for _ in range (tabs_count):
    website = input()
    if website == "Facebook":
        salary -= FACEBOOK
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif website == "Instagram":
        salary -= INSTAGRAM
        if salary <= 0:
            print("You have lost your salary.")
            break
    elif website == "Reddit":
        salary -= REDDIT
        if salary <= 0:
            print("You have lost your salary.")
            break

if salary > 0:
    print(f"{int(salary)}")



