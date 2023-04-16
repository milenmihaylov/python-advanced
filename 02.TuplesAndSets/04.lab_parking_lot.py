parking_lot = set()
for _ in range(int(input())):
    direction, car_number = input().split(', ')
    if direction == 'IN':
        parking_lot.add(car_number)
    elif direction == 'OUT':
        parking_lot.discard(car_number)

if parking_lot:
    [print(car_number) for car_number in parking_lot]
else:
    print("Parking Lot is Empty")
