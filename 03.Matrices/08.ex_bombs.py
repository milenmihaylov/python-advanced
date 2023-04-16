def explosion(i: int, j: int):
    if matrix[i][j] > 0:
        bomb_power = matrix[i][j]
        for i_index in range(i - 1, i + 2):
            if i_index < 0:
                continue
            if i_index < matrix_size:
                for j_index in range(j - 1, j + 2):
                    if j_index < 0:
                        continue
                    if j_index < matrix_size:
                        if matrix[i_index][j_index] > 0:
                            matrix[i_index][j_index] -= bomb_power

                    else:
                        continue

            else:
                continue


matrix_size = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(matrix_size)]
# bombs = [((int(x), int(y)) for x, y in bomb.split(',')) for bomb in input().split()]
# How the next for loop can be writen with comprehension on one line?
bombs = []
for bomb in input().split():
    x, y = bomb.split(',')
    bombs.append((int(x), int(y)))

for bomb in bombs:
    x, y = bomb
    explosion(x, y)

alive_cells = 0
sum_of_cells = 0
for row in matrix:
    for el in row:
        if el > 0:
            alive_cells += 1
            sum_of_cells += el

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_cells}")
[print(' '.join([str(el) for el in row])) for row in matrix]
