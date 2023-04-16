def valid_attack(r, c):
    if r in range(board_size) and c in range(board_size):
        return True
    else:
        return False


def count_attacks(r, c):
    count = 0
    if valid_attack(r - 1, c - 2):
        if board[r - 1][c - 2] == 'K':
            count += 1
    if valid_attack(r - 2, c - 1):
        if board[r - 2][c - 1] == 'K':
            count += 1
    if valid_attack(r - 2, c + 1):
        if board[r - 2][c + 1] == 'K':
            count += 1
    if valid_attack(r - 1, c + 2):
        if board[r - 1][c + 2] == 'K':
            count += 1

    if valid_attack(r + 1, c + 2):
        if board[r + 1][c + 2] == 'K':
            count += 1
    if valid_attack(r + 2, c + 1):
        if board[r + 2][c + 1] == 'K':
            count += 1
    if valid_attack(r + 2, c - 1):
        if board[r + 2][c - 1] == 'K':
            count += 1
    if valid_attack(r + 1, c - 2):
        if board[r + 1][c - 2] == 'K':
            count += 1

    return count


# read the board and collect knights positions
board = []
knights_positions = []
board_size = int(input())
for i in range(board_size):
    row = list(input())
    board.append(row)
    for j in range(len(row)):
        if row[j] == 'K':
            knights_positions.append((i, j))

knights_removed = 0

attacks = {}
conflict = True
while conflict:
    # check each knight how many other knights does attack
    # with 2 funcs 1- for movements and 1 for checking valid movements
    attacks = {(row, col): count_attacks(row, col) for row, col in knights_positions}

    # start removing knights one by one, start with the one, attacking most knights!
    key, value = sorted(attacks.items(), key=lambda x: -x[1])[0]
    key: tuple
    if value > 0:  # still conflict
        knights_positions.remove(key)
        row, col = key
        board[row][col] = '0'
        knights_removed += 1
    else:
        conflict = False  # break

    attacks = {}
    # after each knight out check again if knights are being attacked (its a loop while)
    # if True, repeat, else break and print removed knights count

print(knights_removed)
