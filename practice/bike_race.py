junior_count = int(input())
senior_count = int(input())
trace_type = input()

junior_price = 0
senior_price = 0
total_people = junior_count + senior_count
discount = 1

if trace_type == "trail":
    junior_price = 5.50
    senior_price = 7
elif trace_type == "cross-country":
    junior_price = 8
    senior_price = 9.50
    if total_people >= 50:
        discount = 0.75
elif trace_type == "downhill":
    junior_price = 12.25
    senior_price = 13.75
elif trace_type == "road":
    junior_price = 20
    senior_price = 21.50


total_price = (junior_count * junior_price + senior_count * senior_price) * discount
expenses = total_price * 0.05
final = total_price - expenses

print(f"{final:.2f}")
