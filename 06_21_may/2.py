import sys

count_of_numbers = int(input())
max_number = -sys.maxsize
num_sum = 0

for number in range(count_of_numbers):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number

    num_sum += current_number
rest_sum = num_sum - max_number
if max_number == rest_sum:
    print(f"Yes\nSum = {max_number}")
else:
    difference = abs(max_number - rest_sum)
    print(f"No\nDiff = {difference}")