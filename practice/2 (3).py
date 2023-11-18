shirt_price = float(input())
sum_needed = float(input())

shorts_price = shirt_price * 0.75
socks_price = shorts_price * 0.20
shoes_price = (shirt_price + shorts_price) * 2
totlal_price = shoes_price + socks_price + shorts_price + shirt_price
after_discount = totlal_price * 0.85
if after_discount >= sum_needed:
    print(f"Yes, he will earn the world-cup replica ball!\n"
          f"His sum is {after_discount:.2f} lv.")
else:
    less = sum_needed - after_discount
    print(f"No, he will not earn the world-cup replica ball.\n"
          f"He needs {less:.2f} lv. more.")