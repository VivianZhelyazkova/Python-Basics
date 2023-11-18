command = input()
student = 0
standart = 0
kid = 0
total_tickets = 0
current_tickets = 0
while not command == 'Finish':
    current_tickets = 0
    available_seats = int(input())
    while available_seats > 0:
        action = input()
        total_tickets = available_seats
        if action == 'End':
            break
        if action == "student":
            student += 1
        elif action == 'standart':
            standart += 1
        elif action == 'kid':
            kid += 1
        current_tickets += 1
        available_seats -= 1
    current_percent = current_tickets / total_tickets * 100
    print(f"{command} - {current_percent}% full.")
    command = input()

student_percent  = student / total_tickets
standart_percent = standart / total_tickets
kid_percent = kid / total_tickets
print(f"Total tickets: {total_tickets}")
print(f"{student_percent}% student tickets.")
print(f"{standart_percent}% standart tickets.")
print(f"{kid_percent}% kid tickets.")