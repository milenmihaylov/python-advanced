from collections import deque

total_petrol_pumps = int(input())
petrol_pumps = deque()
for _ in range(total_petrol_pumps):
    petrol_liters, distance = [int(x) for x in input().split()]
    petrol_pumps.append((petrol_liters, distance))

index = 0
fuel_tank = 0
current_index = index
current_iteration_of_pumps = petrol_pumps.copy()
while current_iteration_of_pumps:
    current_petrol_liters, current_distance = current_iteration_of_pumps[0]
    current_index += 1
    if fuel_tank + current_petrol_liters >= current_distance:
        fuel_tank += current_petrol_liters - current_distance
        current_iteration_of_pumps.popleft()
        petrol_pumps.append(petrol_pumps.popleft())

    else:
        petrol_pumps.append(petrol_pumps.popleft())
        current_iteration_of_pumps = petrol_pumps.copy()
        index = current_index
        fuel_tank = 0


print(index)
