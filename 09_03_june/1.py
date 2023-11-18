hour = 0

while hour < 24:
    minutes = 0
    while minutes < 60:
        print(f"{hour:02d}:{minutes:02d}")
        minutes += 1
    hour += 1