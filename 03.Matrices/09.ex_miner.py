def move(direction, current_position):
    i, j = current_position
    if direction == 'left':
        if j > 0:
            return i, j - 1

    elif direction == 'right':
        if j < field_size - 1:
            return i, j + 1

    elif direction == 'up':
        if i > 0:
            return i - 1, j

    elif direction == 'down':
        if i < field_size - 1:
            return i + 1, j

    return current_position

def collecting_coal(current_position):
    if current_position in coals:
        coals.remove(current_position)
        if not coals:
            print(f"You collected all coal! ({current_position[0]}, {current_position[1]})")
            exit()
    elif current_position == end_of_route:
        print(f"Game over! ({current_position[0]}, {current_position[1]})")
        exit()


field_size = int(input())
commands = input().split()
field = []
"""
    • * - a regular position on the field
    • e - the end of the route
    • c - coal
    • s - miner
"""
end_of_route = ()
miner_position = ()
coals = []
for row in range(field_size):
    elements = input().split()
    for col in range(len(elements)):
        el = elements[col]
        if el == 'e':
            end_of_route = (row, col)
        elif el == 's':
            miner_position = (row, col)
        elif el == 'c':
            coals.append((row, col))

for command in commands:
    miner_position = move(command, miner_position)
    collecting_coal(miner_position)

print(f"{len(coals)} pieces of coal left. ({miner_position[0]}, {miner_position[1]})")
