def add(r: int, c: int, val: int, mtrx: list):
    mtrx[r][c] += val
    return mtrx


def subtract(r: int, c: int, val: int, mtrx: list):
    mtrx[r][c] -= val
    return mtrx


matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]

commands = input()
while not commands == 'END':
    command, row, col, value = commands.split()
    row, col, value = int(row), int(col), int(value)
    if row not in range(len(matrix)) or col not in range(len(matrix)):
        print("Invalid coordinates")
    else:
        if command == 'Add':
            matrix = add(row, col, value, matrix)
        elif command == 'Subtract':
            matrix = subtract(row, col, value, matrix)
    commands = input()


[print(' '.join([str(el) for el in row])) for row in matrix]
