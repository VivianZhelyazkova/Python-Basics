age = float(input())
gender = input()
female = "f"
male = "m"

if age >= 16 and gender == male:
    print("Mr.")
elif age < 16 and gender == male:
    print("Master")
if age >= 16 and gender == female:
    print("Ms.")
elif age < 16 and gender == female:
    print("Miss")


