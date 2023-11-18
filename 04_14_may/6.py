n1 = int(input())
n2 = int(input())
operator = input()

operators_list = ["+", "-", "*"]
division_list = ["/", "%"]
if n2 == 0 and operator in division_list:
    print(f"Cannot divide {n1} by zero")

if operator == "+":
    result = n1 + n2
    if (n1 + n2) % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    if result % 2 != 0:
        print(f"{n1} {operator} {n2} = {result} - odd")

if operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")

if operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        print(f"{n1} {operator} {n2} = {result} - even")
    else:
        print(f"{n1} {operator} {n2} = {result} - odd")

if operator == "/" and n2 != 0:
    result = n1 / n2
    print(f"{n1} {operator} {n2} = {result:.2f}")
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")

if operator == "%" and n2 != 0:
    result = n1 % n2
    print(f"{n1} {operator} {n2} = {result}")
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
