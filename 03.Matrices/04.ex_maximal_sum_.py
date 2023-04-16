rows, columns = [int(num) for num in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]
SQUARE_MATRIX_SIZE = 3
max_sum = 0
max_matrix = []
if rows < SQUARE_MATRIX_SIZE:
    first_for_range = 1
else:
    first_for_range = rows - SQUARE_MATRIX_SIZE + 1
if columns < SQUARE_MATRIX_SIZE:
    second_for_range = 1
else:
    second_for_range = columns - SQUARE_MATRIX_SIZE + 1

for i in range(first_for_range):
    if rows < SQUARE_MATRIX_SIZE:
        third_for_range = rows
    else:
        third_for_range = i + SQUARE_MATRIX_SIZE
    for j in range(second_for_range):
        if columns < SQUARE_MATRIX_SIZE:
            forth_for_range = columns
        else:
            forth_for_range = j + SQUARE_MATRIX_SIZE
        current_sum = 0
        current_matrix = []
        for first_index in range(i, third_for_range):
            current_matrix.append([])
            for second_index in range(j, forth_for_range):
                current_sum += matrix[first_index][second_index]
                current_matrix[-1].append(str(matrix[first_index][second_index]))
        if current_sum > max_sum:
            max_sum = current_sum
            max_matrix = current_matrix

print(f"Sum = {max_sum}")
[print(' '.join(el)) for el in max_matrix]
