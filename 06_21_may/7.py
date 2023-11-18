groups_count = int(input())
musala = 0
montblanc = 0
cilimanjaro = 0
k2 = 0
everest = 0
total_people = 0

for _ in range(groups_count):
    current_group = int(input())
    total_people += current_group
    if current_group <= 5:
        musala += current_group
    elif 6 <= current_group <= 12:
        montblanc += current_group
    elif 13 <= current_group <= 25:
        cilimanjaro += current_group
    elif 26 <= current_group <= 40:
        k2 += current_group
    else:
        everest += current_group

musala_percent = musala / total_people * 100
montblanc_percent = montblanc / total_people * 100
cilimanjaro_percent = cilimanjaro / total_people * 100
k2_percent = k2 / total_people * 100
everest_percent = everest / total_people * 100

print(f"{musala_percent:.2f}%\n"
      f"{montblanc_percent:.2f}%")
print(f"{cilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")

