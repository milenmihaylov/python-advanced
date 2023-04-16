from collections import deque
from functools import reduce

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b
}


def calc_eval(sequence: deque, operator: str):
    return reduce(operations[operator], sequence)


expression = deque([el if el in ['+', '-', '*', '/'] else int(el) for el in input().split()])
current_eval = deque()
while True:
    current_symbol = expression.popleft()
    if type(current_symbol) == int:
        current_eval.append(current_symbol)
    else:
        result = int(calc_eval(current_eval, current_symbol))
        if not expression:
            break
        expression.appendleft(result)
        current_eval = deque()

print(int(result))
