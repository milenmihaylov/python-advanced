file = open('numbers.txt', 'r')

result = 0
for num in file:
    result += int(num)

print(result)
