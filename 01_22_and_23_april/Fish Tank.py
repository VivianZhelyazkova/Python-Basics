# 1. Дължина в см – цяло число в интервала [10 … 500]
# 2. Широчина в см – цяло число в интервала [10 … 300]
# 3. Височина в см – цяло число в интервала [10… 200]
# 4. Процент – реално число в интервала [0.000 … 100.000
# Един литър вода се равнява на един кубичен дециметър/ 1л=1 дм3/.

length = int(input())
width = int(input())
height = int(input())
percent = float(input())

volume = int(length * width * height)
liters = float(volume / 1000)
print(liters * (100-percent) / 100)


