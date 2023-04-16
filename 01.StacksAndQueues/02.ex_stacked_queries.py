stack = []
for _ in range(int(input())):
    commands = input().split()
    if commands[0] == '1':
        num = int(commands[1])
        stack.append(num)
    elif commands[0] == '2':
        if stack:
            stack.pop()
    elif commands[0] == '3':
        if stack:
            print(max(stack))
    elif commands[0] == '4':
        if stack:
            print(min(stack))

printable = []
while stack:
    printable.append(str(stack.pop()))
print(', '.join(printable))
