from math import floor,ceil
vineyard = int(input())
grape_per_meter = float(input())
liters_needed = int(input())
workers = int(input())

total_grape = (vineyard * grape_per_meter)
liters_wine = int(floor(0.40 * total_grape / 2.5))

if liters_wine < liters_needed:
    needed = int(floor(liters_needed - liters_wine))
    # needed_as_integer = int(needed)
    print(f"It will be a tough winter! More {needed} liters wine needed.")
else:
    print(f"Good harvest this year! Total wine: {liters_wine} liters.")
    if liters_wine > liters_needed:
        extra = ceil(liters_wine - liters_needed)
        liter_per_worker = ceil(extra / workers)
        print(f"{extra} liters left -> {liter_per_worker} liters per person.")