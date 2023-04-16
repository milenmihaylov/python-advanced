def add(r: int, c: int, val: int):
    if r in range(matrix_size) and c in range(matrix_size):
        matrix[r][c] += val
    else:
        print("Invalid coordinates")


def subtract(r: int, c: int, val: int):
    if r in range(matrix_size) and c in range(matrix_size):
        matrix[r][c] -= val
    else:
        print("Invalid coordinates")


matrix_size = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(matrix_size)]

commands = input()
while not commands == "END":
    command, row, col, value = commands.split()
    if command == "Add":
        add(int(row), int(col), int(value))
    elif command == "Subtract":
        subtract(int(row), int(col), int(value))
    commands = input()

[print(' '.join([str(el) for el in row])) for row in matrix]
