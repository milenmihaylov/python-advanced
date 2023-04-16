from functools import reduce

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '/': lambda a, b: a / b,
    '*': lambda a, b: a * b
}


def operate(operator, *args):
    return reduce(operations[operator], args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
