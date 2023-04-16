def up_direction(r: int, c: int):
    eggs = 0
    positions = []
    for index in range(r-1, -1, -1):
        current_position = field[index][c]
        if type(current_position) is int:
            eggs += current_position
            positions.append([index, c])
        else:
            return {"direction": "up",
                    "eggs": eggs,
                    "positions": positions}
    return {"direction": "up",
            "eggs": eggs,
            "positions": positions}


def down_direction(r: int, c: int):
    eggs = 0
    positions = []
    for index in range(r+1, field_size):
        current_position = field[index][c]
        if type(current_position) is int:
            eggs += current_position
            positions.append([index, c])
        else:
            return {"direction": "down",
                    "eggs": eggs,
                    "positions": positions}
    return {"direction": "down",
            "eggs": eggs,
            "positions": positions}


def left_direction(r: int, c: int):
    eggs = 0
    positions = []
    for index in range(c-1, -1, -1):
        current_position = field[r][index]
        if type(current_position) is int:
            eggs += current_position
            positions.append([r, index])
        else:
            return {"direction": "left",
                    "eggs": eggs,
                    "positions": positions}
    return {"direction": "left",
            "eggs": eggs,
            "positions": positions}


def right_direction(r: int, c: int):
    eggs = 0
    positions = []
    for index in range(c+1, field_size):
        current_position = field[r][index]
        if type(current_position) is int:
            eggs += current_position
            positions.append([r, index])
        else:
            return {"direction": "right",
                    "eggs": eggs,
                    "positions": positions}
    return {"direction": "right",
            "eggs": eggs,
            "positions": positions}


# read the field and find the bunny
field = []
bunny_position = ()

field_size = int(input())
for i in range(field_size):
    field.append([])
    row = input().split()
    for el in row:
        if el.isdigit():
            el = int(el)
        elif el == 'B':
            bunny_position = (i, row.index(el))
        field[-1].append(el)

# go trough each direction and sum the field positions until X or the end of the field
# print the bests

row, col = bunny_position
best = {
    "direction": None,
    "eggs": 0,
    "positions": None}


tmp = up_direction(row, col)
if tmp['eggs'] >= best['eggs']:
    best = tmp
tmp = down_direction(row, col)
if tmp['eggs'] >= best['eggs']:
    best = tmp
tmp = right_direction(row, col)
if tmp['eggs'] >= best['eggs']:
    best = tmp
tmp = left_direction(row, col)
if tmp['eggs'] >= best['eggs']:
    best = tmp

print(best["direction"])
print(*best["positions"], sep='\n')
print(best["eggs"])
