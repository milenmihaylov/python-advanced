from collections import deque

total_petrol_pumps = int(input())
petrol_pumps = deque()
for _ in range(total_petrol_pumps):
    petrol_liters, distance = [int(x) for x in input().split()]
    petrol_pumps.append((petrol_liters, distance))

index = 0
fuel_tank = 0
iteration = 0

while iteration < len(petrol_pumps):
    added_petrol_liters, distance_to_next_pump = petrol_pumps[iteration]
    if fuel_tank + added_petrol_liters >= distance_to_next_pump:
        fuel_tank += added_petrol_liters - distance_to_next_pump
        iteration += 1
    else:
        petrol_pumps.rotate(-1)
        index += 1
        iteration = 0
        fuel_tank = 0

print(index)
