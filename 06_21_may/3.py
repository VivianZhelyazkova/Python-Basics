count_of_numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for _ in range(count_of_numbers):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif 200 <= current_number <= 399:
        p2 += 1
    elif 400 <= current_number <= 599:
        p3 += 1
    elif 600 <= current_number <= 799:
        p4 += 1
    elif 800 <= current_number <= 1000:
        p5 += 1

percent_p1 = p1/count_of_numbers * 100
percent_p2 = p2/count_of_numbers * 100
percent_p3 = p3/count_of_numbers * 100
percent_p4 = p4/count_of_numbers * 100
percent_p5 = p5/count_of_numbers * 100

print(f"{percent_p1:.2f}%")
print(f"{percent_p2:.2f}%")
print(f"{percent_p3:.2f}%")
print(f"{percent_p4:.2f}%")
print(f"{percent_p5:.2f}%")

