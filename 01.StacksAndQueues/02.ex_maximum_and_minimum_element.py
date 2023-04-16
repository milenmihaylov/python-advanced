stack = []

n = int(input())
for _ in range(n):
    query = input().split()  # received query
    type = query[0]  # type of the query
    if type == '1':
        el = int(query[1])
        stack.append(el)
    elif type == '2':
        if stack:
            stack.pop()
    elif type == '3':
        if stack:
            print(max(stack))
    elif type == '4':
        if stack:
            print(min(stack))

printable = []
while stack:
    printable.append(str(stack.pop()))
print(', '.join(printable))
