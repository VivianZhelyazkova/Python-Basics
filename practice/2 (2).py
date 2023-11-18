low_grades = int(input())

problem_count = 0
total_grade = 0
fail = 0
average_score = 0
last_problem = ''
has_failed = True

while fail < low_grades:
    problem = input()
    if problem == "Enough":
        has_failed = False
        break
    grade = int(input())

    if grade <= 4:
        fail += 1
    total_grade += grade
    problem_count += 1
    last_problem = problem

if has_failed:
    print(f"You need a break, {fail} poor grades.")
else:
    average_score = total_grade / problem_count
    print(f"Average score: {average_score:.2f}\n"
          f"Number of problems: {problem_count}\n"
          f"Last problem: {last_problem}")

