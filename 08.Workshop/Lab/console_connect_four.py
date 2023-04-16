def print_board():
    [print(r) for r in board]


def fill_slot(player: int):
    column = input(f"Player {player}, please choose a column\n")
    if not column.isdigit():
        print("Column must be integer in range 1-7 inclusive")
        fill_slot(player)
    else:
        column = int(column)
    if column in range(1, 7 + 1):
        for r in range(5, -1, -1):
            if board[r][column - 1] == 0:
                board[r][column - 1] = player
                break
        else:
            print('Invalid column')
            fill_slot(player)
    else:
        print('Invalid column')
        fill_slot(player)


def check_win():
    winner = check_horizontal()
    if winner:
        return winner
    winner = check_vertical()
    if winner:
        return winner
    winner = check_primary_diagonals()
    if winner:
        return winner
    winner = check_secondary_diagonals()
    if winner:
        return winner
    return False


def check_horizontal():
    for r in range(6):
        for col in range(4):
            if (board[r][col] == board[r][col + 1] == board[r][col + 2] == board[r][col + 3]) and (
                    board[r][col] == 1 or board[r][col] == 2):
                if board[r][col] == 1:
                    return 1
                elif board[r][col] == 2:
                    return 2
    return False


def check_vertical():
    for c in range(7):
        for row in range(3):
            if (board[row][c] == board[row + 1][c] == board[row + 2][c] == board[row + 3][c]) and (
                    board[row][c] == 1 or board[row][c] == 2):
                if board[row][c] == 1:
                    return 1
                elif board[row][c] == 2:
                    return 2
    return False


def check_primary_diagonals():
    for row in range(3):
        for col in range(4):
            try:
                if board[row][col] == board[row + 1][col + 1] == board[row + 2][col + 2] == board[row + 3][col + 3]:
                    if board[row][col] == 1:
                        return 1
                    elif board[row][col] == 2:
                        return 2
            except IndexError:
                continue


def check_secondary_diagonals():
    for row in range(3):
        for col in range(6, 2, -1):
            try:
                if board[row][col] == board[row + 1][col - 1] == board[row + 2][col - 2] == board[row + 3][col - 3]:
                    if board[row][col] == 1:
                        return 1
                    elif board[row][col] == 2:
                        return 2
            except IndexError:
                continue


board = [[0 for _ in range(7)] for _ in range(6)]
print_board()

while True:
    fill_slot(1)
    print_board()
    winning_player = check_win()
    if winning_player:
        print(f"The winner is player {winning_player}")
        break
    fill_slot(2)
    print_board()
    winning_player = check_win()
    if winning_player:
        print(f"The winner is player {winning_player}")
        break
