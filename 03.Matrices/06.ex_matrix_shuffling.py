def check_parameters(input_commands: list):
    if len(input_commands) == 5:
        command, x_1, y_1, x_2, y_2 = input_commands
        if command == 'swap':
            if x_1.isdigit() and y_1.isdigit() and x_2.isdigit() and y_2.isdigit():
                x_1 = int(x_1)
                y_1 = int(y_1)
                x_2 = int(x_2)
                y_2 = int(y_2)
                if x_1 >= 0 and y_1 >= 0 and x_2 >= 0 and y_2 >= 0:
                    if x_1 < rows and y_1 < columns and x_2 < rows and y_2 < columns:
                        return True

    print("Invalid input!")
    return False


def swap_elements(i_1, j_1, i_2, j_2):
    matrix[i_1][j_1], matrix[i_2][j_2] = matrix[i_2][j_2], matrix[i_1][j_1]
    [print(' '.join([str(el) for el in r]) )for r in matrix]


rows, columns = [int(x) for x in input().split()]
matrix = [[row for row in input().split()] for _ in range(rows)]

commands = input().split()
while not commands[0] == 'END':
    if check_parameters(commands):
        i_1, j_1, i_2, j_2 = int(commands[1]), int(commands[2]), int(commands[3]), int(commands[4])
        swap_elements(i_1, j_1, i_2, j_2)
    commands = input().split()
