from math import floor,ceil

magnolia_count = int(input())
hyacinth_count = int(input())
rose_count = int(input())
cactus_count = int(input())
gift_price = float(input())

magnolia_price = 3.25
hyacinth_price = 4
rose_price = 3.50
cactus_price = 8

total_price = magnolia_count * magnolia_price +\
              hyacinth_count * hyacinth_price + \
              rose_count * rose_price + \
              cactus_count * cactus_price
taxes = total_price * 0.05
final = total_price - taxes

if final >= gift_price:
    money_left = int(floor(final - gift_price))
    print(f"She is left with {money_left} leva.")
else:
    money_needed = int(ceil(gift_price - final))
    print(f"She will have to borrow {money_needed} leva." )