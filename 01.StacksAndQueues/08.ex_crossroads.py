from collections import deque


def green_cycle(cars_queue: deque, green_time: int, free_time: int, cars_passed: int = 0):
    while cars_queue and green_time > 0:
        car = cars_queue[0]
        for ch in cars_queue.popleft():
            green_time -= 1
            if green_time < 0:
                free_time -= 1
                if free_time < 0 and ch:
                    print('A crash happened!')
                    print(f"{car} was hit at {ch}.")
                    return 'crash'
        cars_passed += 1
    return cars_passed


green_light = int(input())
free_window = int(input())
cars_queue = deque()
total_cars_passed = 0
command = input()
while not command == 'END':
    if command == 'green':
        result = green_cycle(cars_queue, green_light, free_window)
        if result == 'crash':
            exit()
        else:
            total_cars_passed += result
    else:
        cars_queue.append(command)
    command = input()

print("Everyone is safe.")
print(f"{total_cars_passed} total cars passed the crossroads.")
