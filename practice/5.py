turns = int(input())
total_points = 0
_0_to_9 = 0
_10_to_19 = 0
_20_to_29 = 0
_30_to_39 = 0
_40_to_50 = 0
invalid = 0

for _ in range(1, turns +1):
    points = int(input())
    if 0 <= points <= 9:
        total_points += 0.2 * points
        _0_to_9 += 1
    elif 10 <= points <= 19:
        total_points += 0.3 * points
        _10_to_19 += 1
    elif 20 <= points <= 29:
        total_points += 0.4 * points
        _20_to_29 += 1
    elif 30 <= points <= 39:
        total_points += 50
        _30_to_39 += 1
    elif 40 <= points <= 50:
        total_points += 100
        _40_to_50 += 1
    elif points < 0 or points > 50:
        total_points /= 2
        invalid += 1

_0_to_9_percent = _0_to_9 / turns * 100
_10_to_19_percent = _10_to_19 / turns * 100
_20_to_29_percent = _20_to_29 / turns * 100
_30_to_39_percent = _30_to_39 / turns * 100
_40_to_50_percent = _40_to_50 / turns * 100
invalid_percent = invalid / turns * 100


print(f"{total_points:.2f}\n"
      f"From 0 to 9: {_0_to_9_percent:.2f}%\n"
       f"From 10 to 19: {_10_to_19_percent:.2f}%\n"
       f"From 20 to 29: {_20_to_29_percent:.2f}%\n"
       f"From 30 to 39: {_30_to_39_percent:.2f}%\n"
       f"From 40 to 50: {_40_to_50_percent:.2f}%\n"
       f"Invalid numbers: {invalid_percent:.2f}%")