first_number = int(input())
second_number = int(input())


for number in range(first_number, second_number + 1):
    number_as_str =str(number)
    odd_sum = 0
    even_sum = 0
    for index, digit in enumerate(number_as_str):
        if index % 2 == 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)
    if even_sum == odd_sum:
        print(number, end = " ")

