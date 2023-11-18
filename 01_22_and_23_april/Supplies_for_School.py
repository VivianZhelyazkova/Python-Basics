
pens_price = 5.80
marker_price = 7.20
detergent_price = 1.20

pens = int(input())
markers = int(input())
detergent = int(input())
discount = float(input())
discount_price = float(discount / 100)

total_price = float((pens * pens_price) + (markers * marker_price) + (detergent * detergent_price))
final_discount = float(((pens * pens_price) + (markers * marker_price) + (detergent * detergent_price)) * discount_price)


print(total_price - final_discount)

