n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(input()))
sym = input()
for i in range(n):
    if sym in matrix[i]:
        j = matrix[i].index(sym)
        print(f"({i}, {j})")
        exit()

print(f"{sym} does not occur in the matrix")
