def triangle_line(size):
    line = [str(n) for n in range(1, size + 1)]
    return ' '.join(line)


def print_triangle(size: int):
    for i in range(1, size + 1):
        print(triangle_line(i))
    for m in range(size-1, 0, -1):
        print(triangle_line(m))
