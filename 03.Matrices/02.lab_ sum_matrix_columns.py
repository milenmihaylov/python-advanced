# # using numpy
# from numpy import transpose
#
# rows, columns = input().split(', ')
# matrix = []
# for _ in range(int(rows)):
#     matrix.append([int(el) for el in input().split()])
#
# for t_row in transpose(matrix):
#     print(sum(t_row))

# using zip()
rows, columns = input().split(', ')
matrix = []
for _ in range(int(rows)):
    matrix.append(map(int, input().split()))

for t_row in zip(*matrix):
    print(sum(t_row))
