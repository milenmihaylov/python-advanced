def receive_matrix():
    size = int(input())
    matrix = []
    for _ in range(size):
        matrix.append([int(el) for el in input().split(', ')])
    return matrix


new_matrix = receive_matrix()
even_matrix = [[el for el in row if el % 2 == 0] for row in new_matrix]
print(even_matrix)
