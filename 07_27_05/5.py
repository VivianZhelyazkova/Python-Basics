command = input()
total = 0

while command != "NoMoreMoney":
    current_sum = float(command)
    if current_sum < 0:
        print(f"Invalid operation!")
        break
    command = input()
    total += current_sum
    print(f"Increase: {current_sum:.2f}")


print(f"Total: {total:.2f}")

