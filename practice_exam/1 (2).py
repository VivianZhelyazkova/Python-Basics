name = input()
adult_tickets_count = int(input())
child_tickets_count = int(input())
adult_ticket_price = float(input())
tax = float(input())

child_ticket_price_with_tax = adult_ticket_price * 0.30 + tax
adult_ticket_price_with_tax = adult_ticket_price + tax
total = child_ticket_price_with_tax * child_tickets_count + adult_ticket_price_with_tax * adult_tickets_count
profit = total * 0.20
print(f"The profit of your agency from {name} tickets is {profit:.2f} lv.")