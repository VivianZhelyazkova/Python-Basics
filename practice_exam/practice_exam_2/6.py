first_number = input()
second_number = input()
f1 = 0
f2 = 0
f3 = 0
f4 = 0
s1 = 0
s2 = 0
s3 = 0
s4 = 0

for index,digit in enumerate(first_number):
    if index == 0:
        f1 = int(digit)
    elif index == 1:
        f2 = int(digit)
    elif index == 2:
        f3 = int(digit)
    elif index == 3:
        f4 = int(digit)
for index, digit in enumerate(second_number):
    if index == 0:
        s1 = int(digit)
    elif index == 1:
        s2 = int(digit)
    elif index == 2:
        s3 = int(digit)
    elif index == 3:
        s4 = int(digit)
for f in range(f1,s1 +1):
    for s in range(f2,s2+1):
        for t in range(f3,s3+1):
            for u in range(f4,s4+1):
                if f % 2 != 0 and s % 2 != 0 and t % 2 != 0 and u % 2 != 0:
                    print(f"{f}{s}{t}{u}", end = " ")

