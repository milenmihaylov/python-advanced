def calculate(num_1, num_2, operation):
    if operation == '/':
        try:
            return num_1 / num_2
        except ZeroDivisionError:
            return "Can not divide by zero!"
    elif operation == '*':
        return num_1 * num_2
    elif operation == '-':
        return num_1 - num_2
    elif operation == '+':
        return num_1 + num_2
    elif operation == '^':
        return num_1 ** num_2
    else:
        raise ValueError('Must be valid operator')
