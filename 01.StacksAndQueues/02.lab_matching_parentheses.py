text = input()
stack = []
for index in range(len(text)):
    if text[index] == '(':
        stack.append(index)
    elif text[index] == ')':
        print(text[stack.pop():index+1])

