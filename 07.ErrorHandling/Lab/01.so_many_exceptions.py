import sys
from io import StringIO

test_input = ', '.join(map(str, range(1, 12)))
sys.stdin = StringIO(test_input)

numbers_list = [int(x) for x in test_input.split(", ")]
result = 1

for i in range(len(numbers_list)):
    number = int(numbers_list[i])
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)
