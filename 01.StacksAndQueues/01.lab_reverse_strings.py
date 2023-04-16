word = list(input())
result = ''

while len(word) > 0:
    result += word.pop()

print(result)
