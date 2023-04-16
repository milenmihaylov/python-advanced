rows, columns = input().split(', ')
matrix = []
total_sum = 0
for _ in range(int(rows)):
    row = [int(el) for el in input().split(', ')]
    total_sum += sum(row)
    matrix.append(row)

print(total_sum)
print(matrix)
