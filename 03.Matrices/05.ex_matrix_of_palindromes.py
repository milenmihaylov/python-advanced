from string import ascii_lowercase

r, c = [int(x) for x in input().split()]
matrix = []
for row in range(r):
    matrix.append([])
    for column in range(c):
        matrix[-1].append(ascii_lowercase[row] + ascii_lowercase[row + column] + ascii_lowercase[row])

[print(' '.join(el)) for el in matrix]
