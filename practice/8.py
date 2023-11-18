n = int(input())

equal_values = True
max_difference = 0

for _ in range(n):
    first_num = int(input())
    second_num = int(input())

    pair_sum = first_num + second_num

    if _ > 0 and pair_sum != prev_pair_sum:
        equal_values = False
        difference = abs(pair_sum - prev_pair_sum)
        if difference > max_difference:
            max_difference = difference

    prev_pair_sum = pair_sum

if equal_values:
    print(f"Yes, value={prev_pair_sum}")
else:
    print(f"No, maxdiff={max_difference}")


