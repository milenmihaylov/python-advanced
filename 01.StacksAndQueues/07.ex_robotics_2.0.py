from collections import deque

# create a dict for the robots and their processing time
robots = {}
for rbt in input().split(';'):
    robot_name, process_time = rbt.split('-')
    robots[robot_name] = int(process_time)
free_robots = deque(robots.keys())  # create this list with append method inside the for loop

# reading the time and converting it in seconds
starting_hours, starting_minutes, starting_seconds = input().split(':')
time_in_seconds = ((int(starting_hours) * 60) + int(starting_minutes)) * 60 + int(starting_seconds)

# creating a queue with the given products
products_queue = deque()
product = input()
while not product == "End":
    products_queue.append(product)
    product = input()

working = []
while products_queue:
    time_in_seconds += 1
    if free_robots:
        free_rbt = free_robots.popleft()
        working.append([free_rbt, robots[free_rbt]])
        current_prod = products_queue.popleft()
        hh, mm, ss = [time_in_seconds // 3600, (time_in_seconds % 3600) // 60, (time_in_seconds % 3600) % 60]
        print(f"{free_rbt} - {current_prod} [{hh:02d}:{mm:02d}:{ss:02d}]")

    else:
        products_queue.rotate(-1)

    i = 0
    while i < len(working):
        working[i][1] -= 1
        if working[i][1] <= 0:
            free_robots.append(working[i][0])
            working.pop(i)
            i -= 1
        i += 1

