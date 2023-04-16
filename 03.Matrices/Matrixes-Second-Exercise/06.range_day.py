def shoot_right(r, c):
    for index in range(c, size):
        if shotgun_range[r][index] == "x":
            targets_shot.append([r, index])
            shotgun_range[r][index] = '.'
            return 1
    return 0


def shoot_left(r, c):
    for index in range(c, -1, -1):
        if shotgun_range[r][index] == "x":
            targets_shot.append([r, index])
            shotgun_range[r][index] = '.'
            return 1
    return 0


def shoot_up(r, c):
    for index in range(r, -1, -1):
        if shotgun_range[index][c] == "x":
            targets_shot.append([index, c])
            shotgun_range[index][c] = '.'
            return 1
    return 0


def shoot_down(r, c):
    for index in range(r, size):
        if shotgun_range[index][c] == "x":
            targets_shot.append([index, c])
            shotgun_range[index][c] = '.'
            return 1
    return 0


def move_right(position, s):
    r, c = position
    if c + s in range(size):
        if shotgun_range[r][c + s] == '.':
            shotgun_range[r][c] = '.'
            shotgun_range[r][c + s] = 'A'
            position = (r, c + s)
    return position


def move_left(position, s):
    r, c = position
    r, c = position
    if c - s in range(size):
        if shotgun_range[r][c - s] == '.':
            shotgun_range[r][c] = '.'
            shotgun_range[r][c - s] = 'A'
            position = (r, c - s)
    return position


def move_up(position, s):
    r, c = position
    if r - s in range(size):
        if shotgun_range[r - s][c] == '.':
            shotgun_range[r][c] = '.'
            shotgun_range[r - s][c] = 'A'
            position = (r - s, c)
    return position


def move_down(position, s):
    r, c = position
    if r + s in range(size):
        if shotgun_range[r + s][c] == '.':
            shotgun_range[r][c] = '.'
            shotgun_range[r + s][c] = 'A'
            position = (r + s, c)
    return position


size = 5
shotgun_range = []
my_position = ()
total_targets = 0
targets_shot = []
count_targets = 0
training_completed = False

for i in range(size):
    shotgun_range.append([])
    row = input().split()
    for j in range(len(row)):
        symbol = row[j]
        if symbol == 'A':
            my_position = (i, j)
        elif symbol == "x":
            total_targets += 1
        shotgun_range[-1].append(symbol)

for _ in range(int(input())):
    commands = input().split()
    action = commands[0]
    direction = commands[1]
    if action == 'move':
        steps = int(commands[2])
        if direction == 'right':
            my_position = move_right(my_position, steps)
        elif direction == 'left':
            my_position = move_left(my_position, steps)
        elif direction == 'up':
            my_position = move_up(my_position, steps)
        elif direction == 'down':
            my_position = move_down(my_position, steps)

    elif action == 'shoot':
        if direction == 'right':
            count_targets += shoot_right(my_position[0], my_position[1])
        elif direction == 'left':
            count_targets += shoot_left(my_position[0], my_position[1])
        elif direction == 'up':
            count_targets += shoot_up(my_position[0], my_position[1])
        elif direction == 'down':
            count_targets += shoot_down(my_position[0], my_position[1])

        if count_targets == total_targets:
            training_completed = True
            break

if training_completed:
    print(f"Training completed! All {count_targets} targets hit.")
else:
    print(f"Training not completed! {total_targets - count_targets} targets left.")

print(*targets_shot, sep='\n')

