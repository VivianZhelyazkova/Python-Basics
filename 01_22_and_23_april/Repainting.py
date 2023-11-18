
PROTECTIVE_NYLON = float(1.50)
PAINT = float(14.50)
PAINT_THINNER = float(5.00)
BAGS = float(0.40)

nylon_count =float(input())
paint_count = float(input())
paint_thinner_count = float(input())
hours_needed = float(input())

total_nylon = (nylon_count +2) * PROTECTIVE_NYLON
total_paint = (paint_count * 1.1 )* PAINT

total_price = float(total_paint + total_nylon + paint_thinner_count * PAINT_THINNER + BAGS)
workers_price = float(total_price * 0.3) * hours_needed

print(float(total_price + workers_price))