capacity = int(input())
fans = int(input())
a_sector = 0
b_sector = 0
v_sector = 0
g_sector = 0
for _ in range(1,fans + 1):
    sector = input()
    if sector == "A":
        a_sector += 1
    elif sector == "B":
        b_sector += 1
    elif sector == "V":
        v_sector += 1
    elif sector == "G":
        g_sector += 1

a_percent = a_sector / fans * 100
b_percent = b_sector / fans * 100
v_percent = v_sector / fans * 100
g_percent = g_sector / fans * 100
total_percent = fans / capacity * 100

print(f"{a_percent:.2f}%\n"
      f"{b_percent:.2f}%\n"
      f"{v_percent:.2f}%\n"
      f"{g_percent:.2f}%\n"
      f"{total_percent:.2f}%")