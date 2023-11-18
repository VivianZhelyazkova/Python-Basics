number = int(input())
combinations = 0
for x1 in range(number + 1):
    for x2 in range(number + 1):
        for x3 in range(number + 1):
            sum = x1 + x2 + x3
            if sum == number:
                combinations += 1

print(combinations)
