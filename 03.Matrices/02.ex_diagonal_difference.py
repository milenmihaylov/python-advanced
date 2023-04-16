n = int(input())
matrix = []
sum_primary_diagonal = 0
sum_secondary_diagonal = 0
for i in range(n):
    matrix.append([int(el) for el in input().split()])
    sum_primary_diagonal += matrix[i][i]
    sum_secondary_diagonal += matrix[i][~i]
    # print(f'i = {i}')
    # print(f'~i = {~i}')

print(abs(sum_primary_diagonal - sum_secondary_diagonal))
