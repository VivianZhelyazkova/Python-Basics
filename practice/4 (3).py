students_count = int(input())
top = 0
between_4_499 = 0
between_3_399 = 0
fail = 0
total = 0

for student in range(students_count):
    grade = float(input())
    if grade >= 5:
        top += 1
        total += grade
    elif grade >= 4:
        between_4_499 += 1
        total += grade
    elif grade >= 3:
        between_3_399 += 1
        total += grade
    else:
        fail += 1
        total += grade
average_grade = total / students_count
top_percent = top / students_count * 100
between_3_399_percent = between_3_399 / students_count * 100
between_4_499_percent = between_4_499 / students_count * 100
fail_percent = fail / students_count * 100
print(f'Top students: {top_percent:.2f}%')
print(f'Between 4.00 and 4.99: {between_4_499_percent:.2f}%')
print(f'Between 3.00 and 3.99: {between_3_399_percent:.2f}%')
print(f'Fail: {fail_percent:.2f}%')
print(f'Average: {average_grade:.2f}')


