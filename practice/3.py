loads = int(input())


BUS = 200
TRUCK = 175
TRAIN = 120
price_bus = 0
price_truck = 0
price_train = 0
loads_tons = 0
bus_count = 0
truck_count = 0
train_count = 0

for _ in range(1,loads +1):
    tons = int(input())
    if tons <= 3:
        price_bus += tons * BUS
        loads_tons += tons
        bus_count += tons
    elif 4 <= tons <= 11:
        price_truck += tons * TRUCK
        loads_tons += tons
        truck_count += tons
    else:
        price_train += tons * TRAIN
        loads_tons += tons
        train_count += tons
total = price_bus + price_truck + price_train
average_price = total / loads_tons
bus_percent = bus_count / loads_tons * 100
truck_percent = truck_count / loads_tons * 100
train_percent = train_count / loads_tons * 100

print(f"{average_price:.2f}\n"
      f"{bus_percent:.2f}%\n"
      f"{truck_percent:.2f}%\n"
      f"{train_percent:.2f}%")