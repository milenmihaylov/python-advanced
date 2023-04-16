matrix = []
rows, columns = [int(x) for x in input().split(', ')]
for _ in range(rows):
    matrix.append([int(el) for el in input().split(', ')])

max_sum = 0
best_2x2_matrix = []
for i in range(rows - 1):
    for j in range(columns - 1):
        a_11 = matrix[i][j]
        a_12 = matrix[i][j + 1]
        a_21 = matrix[i + 1][j]
        a_22 = matrix[i + 1][j + 1]
        a_sum = a_11 + a_12 + a_21 + a_22
        if a_sum > max_sum:
            max_sum = a_sum
            best_2x2_matrix = [[a_11, a_12],
                               [a_21, a_22]]

for el in best_2x2_matrix:
    print(' '.join(map(str, el)))
print(max_sum)
