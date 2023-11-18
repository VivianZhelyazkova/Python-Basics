first_number_final = int(input())
second_number_final = int(input())
third_number_final = int(input())
is_even = True
is_prime = True
for first_number in range(1, first_number_final+ 1):
    if first_number % 2 != 0:
        is_even = False
        continue
    for second_number in range(1, second_number_final + 1):
        if second_number == 2 or second_number == 3 or second_number == 5 or second_number == 7:
            is_prime = True
        else:
            is_prime = False
            continue
        for third_number in range(1, third_number_final + 1):
            if third_number % 2 != 0:
                is_even = False
                continue
            print(first_number, second_number, third_number)
