
budget = float(input())
video_card_count = int(input())
processor_count = int(input())
ram_count = int(input())

video_card_price = 250
processor_price = video_card_count * video_card_price * 0.35
ram_price = video_card_count * video_card_price * 0.10

total_cost = video_card_count * video_card_price \
             + processor_count * processor_price \
             + ram_count * ram_price
if video_card_count > processor_count:
    total_cost *= (1-0.15)

if budget >= total_cost:
    print(f"You have {budget - total_cost:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_cost - budget:.2f} leva more!")

