def next_move(direction, position: tuple):
    i, j = position
    if direction == 'L':
        if j == 0:
            lair[i][j] = '.'
            return True, position
        else:
            position = (i, j - 1)
            lair[i][j] = '.'
            if lair[i][j - 1] == '.':
                lair[i][j - 1] = 'P'

    elif direction == 'R':
        if j == columns - 1:
            lair[i][j] = '.'
            return True, position
        else:
            position = (i, j + 1)
            lair[i][j] = '.'
            if lair[i][j + 1] == '.':
                lair[i][j + 1] = 'P'
    elif direction == 'U':
        if i == 0:
            lair[i][j] = '.'
            return True, position
        else:
            position = (i - 1, j)
            lair[i][j] = '.'
            if lair[i - 1][j] == '.':
                lair[i - 1][j] = 'P'
    elif direction == 'D':
        if i == rows - 1:
            lair[i][j] = '.'
            return True, position
        else:
            position = (i + 1, j)
            lair[i][j] = '.'
            if lair[i + 1][j] == '.':
                lair[i + 1][j] = 'P'
    return False, position


def bunnies_f_cking():
    new_bunnies = set()
    for a, b in bunnies_positions:
        if a > 0:
            new_bunnies.add((a - 1, b))
            lair[a - 1][b] = 'B'
        if a < rows-1:
            new_bunnies.add((a + 1, b))
            lair[a + 1][b] = 'B'
        if b > 0:
            new_bunnies.add((a, b - 1))
            lair[a][b-1] = 'B'
        if b < columns-1:
            new_bunnies.add((a, b + 1))
            lair[a][b+1] = 'B'
    return new_bunnies


lair = []
player_position = ()
bunnies_positions = set()
player_won = False
player_died = False

# reading the field
rows, columns = [int(x) for x in input().split()]
for r in range(rows):
    lair.append([])
    row = input()
    for c in range(columns):
        el = row[c]
        lair[-1].append(el)
        if el == 'P':
            player_position = (r, c)
        elif el == 'B':
            bunnies_positions.add((r, c))

# reading commands and executing them
commands = input()
for command in commands:
    player_won, player_position = next_move(command, player_position)

    bunnies_positions = bunnies_positions | bunnies_f_cking()
    if player_won:
        break
    if player_position in bunnies_positions:
        player_died = True
        break

# printing the result
[print(''.join(row)) for row in lair]
if player_won:
    print(f"won: {player_position[0]} {player_position[1]}")
elif player_died:
    print(f"dead: {player_position[0]} {player_position[1]}")
