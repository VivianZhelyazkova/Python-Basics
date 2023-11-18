num = int(input())
for number in range(1_111,10_000):
    number_as_string = str(number)
    is_special = True
    for _ ,digit in enumerate(number_as_string):
        digit_as_int = int(digit)
        if digit_as_int == 0:
            is_special = False
            break
        if not num % digit_as_int == 0:
            is_special = False
            break
    if is_special:
        print(number, end=' ')

