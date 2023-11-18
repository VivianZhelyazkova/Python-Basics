chrysanthemum_count = int(input())
rose_count = int(input())
tulip_count = int(input())
season = input()
day = input()

chrysanthemum_price = 0
rose_price = 0
tulip_price = 0
discount = 1
second_discount = 1
arangement = 2.00

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2.00
    rose_price = 4.10
    tulip_price = 2.50
    if season == "Spring" and tulip_count > 7:
        discount = 0.95
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15
    if season == "Winter" and rose_count >=10:
        discount = 0.90
if day == "Y":
    increase = 1.15
else:
    increase = 1
if chrysanthemum_count + rose_count + tulip_count > 20:
    second_discount = 0.80

total_price =  chrysanthemum_count * chrysanthemum_price + rose_count * rose_price + tulip_count * tulip_price
after_discount = total_price * increase * discount * second_discount + arangement

print(f"{after_discount:.2f}")