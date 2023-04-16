def cookie(position: tuple, presents, kids):
    r, c = position
    go_to_position.append(position)
    if r - 1 in range(neighborhood_size):
        if neighborhood[r - 1][c] == 'V':
            presents -= 1
            kids -= 1
            # forbidden_positions.append((r - 1, c))
        elif neighborhood[r - 1][c] == 'X':
            presents -= 1
            # forbidden_positions.append((r - 1, c))
        neighborhood[r - 1][c] = '-'
        # ако стъпиш пак се връща; на това мястно

    if r + 1 in range(neighborhood_size):
        if neighborhood[r + 1][c] == 'V':
            presents -= 1
            kids -= 1
            # forbidden_positions.append((r + 1, c))
        elif neighborhood[r + 1][c] == 'X':
            presents -= 1
            # forbidden_positions.append((r + 1, c))
        neighborhood[r - 1][c] = '-'

    if c - 1 in range(neighborhood_size):
        if neighborhood[r][c - 1] == 'V':
            presents -= 1
            kids -= 1
            # forbidden_positions.append((r, c - 1))
        elif neighborhood[r][c - 1] == 'X':
            presents -= 1
            # forbidden_positions.append((r, c - 1))
        neighborhood[r][c - 1] = '-'
    if c + 1 in range(neighborhood_size):
        if neighborhood[r][c + 1] == 'V':
            presents -= 1
            kids -= 1
            # forbidden_positions.append((r, c + 1))
        elif neighborhood[r][c + 1] == 'X':
            presents -= 1
            # forbidden_positions.append((r, c + 1))
        neighborhood[r][c + 1] = '-'

    return presents, kids


def up(position: tuple, presents, kids):
    r, c = position
    if r - 1 in range(neighborhood_size):
        neighborhood[r][c] = '-'
        tmp_el = neighborhood[r - 1][c]
        position = (r - 1, c)
        if position in forbidden_positions:
            position = go_to_position[0]
            neighborhood[position[0]][position[1]] = 'S'
            return position, presents, kids
        if tmp_el == 'V':
            presents -= 1
            kids -= 1
        elif tmp_el == 'C':
            presents, kids = cookie(position, presents, kids)
        neighborhood[r - 1][c] = 'S'
    return position, presents, kids


def down(position: tuple, presents, kids):
    r, c = position
    if r + 1 in range(neighborhood_size):
        neighborhood[r][c] = '-'
        tmp_el = neighborhood[r + 1][c]
        position = (r + 1, c)
        if position in forbidden_positions:
            position = go_to_position[0]
            neighborhood[position[0]][position[1]] = 'S'
            return position, presents, kids
        if tmp_el == 'V':
            presents -= 1
            kids -= 1
        elif tmp_el == 'C':
            presents, kids = cookie(position, presents, kids)
        neighborhood[r + 1][c] = 'S'
    return position, presents, kids


def left(position: tuple, presents, kids):
    r, c = position
    if c - 1 in range(neighborhood_size):
        neighborhood[r][c] = '-'
        tmp_el = neighborhood[r][c - 1]
        position = (r, c - 1)
        if position in forbidden_positions:
            position = go_to_position[0]
            neighborhood[position[0]][position[1]] = 'S'
            return position, presents, kids
        if tmp_el == 'V':
            presents -= 1
            kids -= 1
        elif tmp_el == 'C':
            presents, kids = cookie(position, presents, kids)
        neighborhood[r][c - 1] = 'S'
    return position, presents, kids


def right(position: tuple, presents, kids):
    r, c = position
    if c + 1 in range(neighborhood_size):
        neighborhood[r][c] = '-'
        tmp_el = neighborhood[r][c + 1]
        position = (r, c + 1)
        if position in forbidden_positions:
            position = go_to_position[0]
            neighborhood[position[0]][position[1]] = 'S'
            return position, presents, kids
        if tmp_el == 'V':
            presents -= 1
            kids -= 1
        elif tmp_el == 'C':
            presents, kids = cookie(position, presents, kids)
        neighborhood[r][c + 1] = 'S'
    return position, presents, kids


number_of_presents = int(input())
neighborhood_size = int(input())
neighborhood = []
santa_position = ()
nice_kids_count = 0

forbidden_positions = []
go_to_position = []

for i in range(neighborhood_size):
    neighborhood.append([])
    row = input().split()
    for j in range(neighborhood_size):
        el = row[j]
        if el == 'V':
            nice_kids_count += 1
        elif el == 'S':
            santa_position = (i, j)
        neighborhood[-1].append(el)

count_nice_kids = nice_kids_count
command = input()
while not command == "Christmas morning":
    if command == "up":
        santa_position, number_of_presents, nice_kids_count = up(santa_position, number_of_presents, nice_kids_count)
        if number_of_presents <= 0:
            break
    elif command == "down":
        santa_position, number_of_presents, nice_kids_count = down(santa_position, number_of_presents, nice_kids_count)
        if number_of_presents <= 0:
            break
    elif command == "left":
        santa_position, number_of_presents, nice_kids_count = left(santa_position, number_of_presents, nice_kids_count)
        if number_of_presents <= 0:
            break
    elif command == "right":
        santa_position, number_of_presents, nice_kids_count = right(santa_position, number_of_presents, nice_kids_count)
        if number_of_presents <= 0:
            break
    command = input()

if number_of_presents <= 0:
    print("Santa ran out of presents!")
[print(' '.join(x)) for x in neighborhood]
if nice_kids_count <= 0:
    print(f"Good job, Santa! {count_nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids_count} nice kid/s.")
