from math import ceil


def choose_symbol(player_1_name):
    player_one_choice = input(f"{player_1_name} would you like to play with 'X' or 'O'? ")
    if player_one_choice.upper() == 'X':
        player_1_symbol, player_2_symbol = 'X', 'O'
        return player_1_symbol, player_2_symbol
    elif player_one_choice.upper() == 'O':
        player_1_symbol, player_2_symbol = 'O', 'X'
        return player_1_symbol, player_2_symbol
    else:
        print('The signs can only be "X" and "O"')
        return choose_symbol(player_1_name)


def print_board(game_board):
    [print('|  ' + '  |  '.join(x) + '  |') for x in game_board]


def print_initial_board(game_board):
    print("This is the numeration of the board:")
    [print(x) for x in game_board]


def play(board, player, symbol):
    print(f"{player} choose free position [1-9]:")
    position = input()
    if not position.isdigit() or int(position) not in range(1, 10):
        print("Please, enter an integer [1-9]:")
        play(board, player, symbol)
    position = int(position)
    row = ceil(position / 3) - 1
    col = position % 3 - 1
    if check_free_position(row, col, position):
        board[row][col] = symbol
        play(board, player, symbol)



def check_free_position(row, col, position):
    if board[row][col] == ' ':
        return True
    print(f"Position {position} is not free!")
    return False


def check_won(player, player_symbol):
    first_row = all(x == player_symbol for x in board[0])
    second_row = all(x == player_symbol for x in board[1])
    third_row = all(x == player_symbol for x in board[2])
    first_column = all(x == player_symbol for x in [board[0][0], board[1][0], board[2][0]])
    second_column = all(x == player_symbol for x in [board[0][1], board[1][1], board[2][1]])
    third_column = all(x == player_symbol for x in [board[0][2], board[1][2], board[2][2]])
    first_diagonal = all(x == player_symbol for x in [board[0][0], board[1][1], board[2][2]])
    second_diagonal = all(x == player_symbol for x in [board[0][2], board[1][1], board[2][0]])
    if any([first_row, second_row, third_row, first_column, second_column, third_column,
            first_diagonal, second_diagonal]):
        print(f"{player} won!")
        return True
    return False


initial_board = [
    '|  1  |  2  |  3  |',
    '|  4  |  5  |  6  |',
    '|  7  |  8  |  9  |']

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']]

player_one_name = input("Player one name: ")
player_two_name = input("Player two name: ")
player_one_symbol, player_two_symbol = choose_symbol(player_one_name)
print_initial_board(initial_board)
current, other = (player_one_name, player_one_symbol), (player_two_name, player_two_symbol)

print(f"{player_one_name} starts first!")
while True:
    play(board, current[0], current[1])
    print_board(board)
    if check_won(current[0], current[1]):
        break
    current, other = other, current
