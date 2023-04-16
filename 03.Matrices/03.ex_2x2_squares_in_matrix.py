rows, columns = [int(num) for num in input().split()]
matrix = [[el for el in input().split()] for _ in range(rows)]
total_square_matrices = 0
for i in range(rows - 1):
    for j in range(columns - 1):
        a_11 = matrix[i][j]
        a_12 = matrix[i][j+1]
        a_21 = matrix[i+1][j]
        a_22 = matrix[i+1][j+1]
        if a_11 == a_12 == a_21 == a_22:
            total_square_matrices += 1

print(total_square_matrices)
