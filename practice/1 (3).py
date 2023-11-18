
processor_dollars = float(input())
video_card_dollars = float(input())
ram_dollars = float(input())
ram_count = int(input())
discount = float(input())

processor_leva = processor_dollars * 1.57 * (1 - discount)
video_card_leva = video_card_dollars * 1.57 * (1 - discount)
ram_leva = ram_dollars * 1.57
total_ram_leva = ram_leva * ram_count
total_leva = processor_leva + video_card_leva + total_ram_leva

print(f"Money needed - {total_leva:.2f} leva.")