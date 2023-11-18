import sys
numbers = int(input())

odd_sum = 0
even_sum = 0
lowest_odd = 0
highest_odd = 0
lowest_even = 0
highest_even = 0

lowest_odd = sys.maxsize
highest_odd = -sys.maxsize
lowest_even = sys.maxsize
highest_even = -sys.maxsize

for i in range(1,numbers + 1):
    current_number = float(input())
    if i % 2 != 0:
        odd_sum += current_number
        if current_number > highest_odd:
            highest_odd = current_number
        if current_number < lowest_odd:
            lowest_odd = current_number
       
    if i % 2 == 0:
        even_sum += current_number
        if current_number > highest_even:
            highest_even = current_number
        if current_number < lowest_even:
            lowest_even = current_number
if lowest_odd == sys.maxsize:
    lowest_odd = "No"
    highest_odd = "No"
if lowest_even == sys.maxsize:
    lowest_even = "No"
    highest_even = "No"
if isinstance(lowest_odd, float):
    lowest_odd = f"{lowest_odd:.2f}"
if isinstance(highest_odd, float):
    highest_odd = f"{highest_odd:.2f}"
if isinstance(lowest_even, float):
    lowest_odd = f"{lowest_odd:.2f}"
if isinstance(highest_even, float):
    highest_even = f"{highest_even:.2f}"
print(f"OddSum={odd_sum:.2f},\n"
    f"OddMin={lowest_odd},\n"
    f"OddMax={highest_odd},\n"
    f"EvenSum={even_sum:.2f},\n"
    f"EvenMin={lowest_even},\n"
    f"EvenMax={highest_even}")

