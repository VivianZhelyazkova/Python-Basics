first_final = int(input())
second_final = int(input())
third_final = int(input())
for f in range(1, first_final + 1):
    if f % 2 == 0:
        for s in range(1, second_final + 1):
            if s == 2 or s == 3 or s == 5 or s == 7:
                for t in range(1, third_final + 1):
                    if t % 2 == 0:
                        print(f, s, t,end = "")
                        print()