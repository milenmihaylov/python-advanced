n = int(input())
matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]

primary_diagonal = []
secondary_diagonal = []
sum_primary_diagonal = 0
sum_secondary_diagonal = 0

for i in range(n):
    el_primary = matrix[i][i]
    primary_diagonal.append(str(el_primary))
    sum_primary_diagonal += el_primary

    el_secondary = matrix[i][~i]
    secondary_diagonal.append(str(el_secondary))
    sum_secondary_diagonal += el_secondary

print(f"Primary diagonal: {', '.join(primary_diagonal)}. Sum: {sum_primary_diagonal}")
print(f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {sum_secondary_diagonal}")
