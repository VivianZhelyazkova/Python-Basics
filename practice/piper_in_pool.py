from multiprocessing import pool

pool_volume = int(input())
pipe_one = int(input())
pipe_two = int(input())
hours = float(input())

pipe_one_total = pipe_one * hours
pipe_two_total = pipe_two * hours
percent_both = (pipe_one_total + pipe_two_total) / pool_volume * 100
both = pipe_one_total + pipe_two_total
pipe_one_percent = pipe_one_total / both * 100
pipe_two_percent = pipe_two_total / both * 100

if both <= pool_volume:
    print(f"The pool is {percent_both}% full. Pipe 1: {pipe_one_percent:.2f}%. Pipe 2: {pipe_two_percent:.2f}%.")
else:
    print(f"For {hours} hours the pool overflows with {both - pool_volume:.2f} liters.")