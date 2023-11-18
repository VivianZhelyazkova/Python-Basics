# • Пилешко меню – 10.35 лв.
# • Меню с риба – 12.40 лв.
# • Вегетарианско меню – 8.15 лв.

chicken_menu_price = float(10.35)
fish_menu_price = float(12.40)
vegi_menu_price = float(8.15)
delivery = float(2.50)

chicken_menu_price_count = float(input())
fish_menu_price_count = float(input())
vegi_menu_price_count = float(input())

bill = (float(chicken_menu_price_count * chicken_menu_price + fish_menu_price_count * fish_menu_price + vegi_menu_price_count * vegi_menu_price))

dessert = float(bill * 0.2)

print(float(bill + dessert + delivery))
