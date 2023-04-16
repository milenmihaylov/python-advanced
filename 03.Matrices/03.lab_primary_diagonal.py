n = int(input())
matrix = []
total_sum = 0
for i in range(n):
    matrix.append(list(map(int, input().split())))
    total_sum += matrix[i][i]

print(total_sum)
