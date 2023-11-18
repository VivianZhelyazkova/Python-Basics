
jury_count = int(input())
presentation = input()
total_grade = 0
grade_count = 0
sum_of_grades = 0
while not presentation == "Finish":
    for i in range(jury_count):
        grade = float(input())
        total_grade += grade
        grade_count += 1
        sum_of_grades += grade
    average_grade = total_grade / jury_count
    print(f"{presentation} - {average_grade:.2f}.")
    total_grade = 0
    presentation = input()

total_average = sum_of_grades / grade_count

print(f"Student's final assessment is {total_average:.2f}.")

