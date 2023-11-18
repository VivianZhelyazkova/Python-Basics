# 1. Брой страници в текущата книга – цяло число в интервала [1…1000]
#
# 2. Страници, които прочита за 1 час – цяло число в интервала [1…1000]
#
# 3. Броят на дните, за които трябва да прочете книгата – цяло число в интервала [1…1000]

pages_total = int(input())
pages_per_hour = int(input())
days = int(input())

total_hours = pages_total / pages_per_hour
hours_per_day = total_hours / days

print(int(hours_per_day))