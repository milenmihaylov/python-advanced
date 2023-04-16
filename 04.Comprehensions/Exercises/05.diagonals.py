matrix = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]
first_diagonal = []
second_diagonal = []
sum_first_diagonal = 0
sum_second_diagonal = 0
for i in range(len(matrix)):
    first_diagonal.append(str(matrix[i][i])), second_diagonal.append(str(matrix[i][~i]))
    sum_first_diagonal += matrix[i][i]
    sum_second_diagonal += matrix[i][~i]
print(f"First diagonal: {', '.join(first_diagonal)}. Sum: {sum_first_diagonal}")
print(f"Second diagonal: {', '.join(second_diagonal)}. Sum: {sum_second_diagonal}")
