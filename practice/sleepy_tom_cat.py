rest_days = int(input())

norm_for_play = 30000

working_days = 365 - rest_days

rest_days_play_time = rest_days * 127
working__play_time = working_days * 63
total_play_time = working__play_time + rest_days_play_time
more = total_play_time - norm_for_play
if total_play_time > norm_for_play:
    hours = more // 60
    minutes = more % 60
    print(f"Tom will run away\n"
          f"{hours} hours and {minutes} minutes more for play")
else:
    less = norm_for_play - total_play_time
    hours = less // 60
    minutes = less % 60
    print(f"Tom sleeps well\n"
          f"{hours} hours and {minutes} minutes less for play")