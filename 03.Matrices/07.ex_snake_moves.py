from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = deque(input())
matrix = []
for i in range(rows):
    matrix.append([])
    for j in range(columns):
        ch = snake.popleft()
        snake.append(ch)
        if i % 2 == 0:
            matrix[-1].append(ch)
        else:
            matrix[-1].insert(0, ch)

[print(''.join(el)) for el in matrix]
