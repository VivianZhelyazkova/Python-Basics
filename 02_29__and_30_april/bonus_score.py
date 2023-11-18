points = int(input())
bonus = 0
second_bonus = 0

if points <= 100:
    bonus = 5
elif points <= 1000:
    bonus = points * 0.2
else:
    bonus = points * 0.1

if points % 2 == 0:
    second_bonus = 1
if points % 10 == 5:
    second_bonus = 2

print(bonus + second_bonus)
print(points + bonus + second_bonus)
