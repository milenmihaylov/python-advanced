from collections import deque


def math_operations(*args, a, s, d, m):
    dictionary = {}
    keys = deque(['a', 's', 'd', 'm'])
    for index in range(len(args)):
        key = keys.popleft()
        keys.append(key)
        dictionary[key]
        dictionary = {
            'a': a + args[0],
            's': s - args[1],
            'd': d / args[2],
            'm': m * args[3]
        }
        args = args[4:]

    return dictionary


# print(math_operations(2, 12, 0, -3, 6, -20,  -11, a=1, s=7, d=33, m=15))
# print(math_operations(-1, 0, 1, 0, 6, -2, 80, a=0, s=0, d=0, m=0))
print(math_operations(6, a=0, s=0, d=0, m=0))
