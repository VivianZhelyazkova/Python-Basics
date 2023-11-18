
bitcoins = int(input())
junas = float(input())
commission = float(input())

bitcoin_price = 1168 * bitcoins
junas_dolars = junas * 0.15
dollars_to_leva = junas_dolars * 1.76
total = bitcoin_price + dollars_to_leva
euro = total / 1.95
commission_total = euro * (commission / 100)
final = euro - commission_total
print(f"{final:.2f}")