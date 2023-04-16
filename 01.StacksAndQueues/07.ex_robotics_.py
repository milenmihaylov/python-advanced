from collections import deque

robots = deque()
products_line = deque()
working_robots = []
for el in input().split(';'):
    robot_name, process_time = el.split('-')
    robots.append((robot_name, int(process_time)))

starting_hours, starting_minutes, starting_seconds = input().split(':')
time_in_seconds = ((int(starting_hours) * 60) + int(starting_minutes)) * 60 + int(starting_seconds)

receiving_products = True
product = input()

while products_line:
    if product == "End" and len(products_line):
        break
    if not product == "End":
        products_line.append(product)
    time_in_seconds += 1
    hh, mm, ss = [time_in_seconds // 3600, (time_in_seconds % 3600) // 60, (time_in_seconds % 3600) % 60]
    if robots:  # if free_robots
        robot_name, robot_process_time = robots.popleft()
        working_robots.append([robot_name, robot_process_time, robot_process_time])
        print(f'{robot_name} - {products_line.popleft()} [{hh:02d}:{mm:02d}:{ss:02d}]')
    else:
        products_line.rotate(-1)
    n = len(working_robots)
    index = 0
    for _ in range(n):
        if index >= len(working_robots):
            break
        working_robots[index][2] -= 1
        if working_robots[index][2] <= 0:
            robots.append((working_robots[index][0], working_robots[index][1]))
            working_robots.pop(index)
            index -= 1
        index += 1

    if receiving_products:
        product = input()
        if not product == 'End':
            products_line.appendleft(product)
        else:
            receiving_products = False
