students = int(input())
a_students = 0
b_students = 0
c_students = 0
d_students = 0
total_grade = 0

for _ in range(1,students+1):
    grade = float(input())
    if grade >= 5.00:
        a_students += 1
        total_grade += grade
    elif 4.00 <= grade <= 4.99:
        b_students += 1
        total_grade += grade
    elif 3.00 <= grade <= 3.99:
        c_students += 1
        total_grade += grade
    elif grade < 3.00:
        d_students += 1
        total_grade += grade

a_percent = a_students / students * 100
b_percent = b_students / students * 100
c_percent = c_students / students * 100
d_percent = d_students / students * 100
average_grade = total_grade / students

print(f"Top students: {a_percent:.2f}%\n"
     f"Between 4.00 and 4.99: {b_percent:.2f}%\n"
     f"Between 3.00 and 3.99: {c_percent:.2f}%\n"
     f"Fail: {d_percent:.2f}%\n"
     f"Average: {average_grade:.2f}")

