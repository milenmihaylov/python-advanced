from collections import deque

cups_capacity = deque([int(cup) for cup in input().split()])
water_in_bottles = [int(bottle) for bottle in input().split()]

wasted_liters = 0
while cups_capacity and water_in_bottles:
    # cup = cups_capacity[0]
    bottle = water_in_bottles.pop()
    cups_capacity[0] -= bottle
    if cups_capacity[0] <= 0:
        wasted_liters += abs(cups_capacity[0])
        cups_capacity.popleft()

printable = []
if not cups_capacity:
    while water_in_bottles:
        printable.append(str(water_in_bottles.pop()))
    print(f"Bottles: {' '.join(printable)}")
elif not water_in_bottles:
    while cups_capacity:
        printable.append(str(cups_capacity.popleft()))
    print(f"Cups: {' '.join(printable)}")

print(f"Wasted litters of water: {wasted_liters}")
