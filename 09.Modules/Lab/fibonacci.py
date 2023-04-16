# for-loop:
def fibonacci_sequence(total_numbers: int):
    """
    :param total_numbers: positive integer, the first count of numbers from the fibonacci sequence
    :return: list of the first {total_numbers} of the fibonacci numbers
    """
    first_num = 0
    second_num = 1
    fib_list = [first_num, second_num]
    for _ in range(total_numbers - 1):
        first_num, second_num = second_num, second_num + first_num
        fib_list.append(second_num)
    return fib_list


def fibonacci_number(n):
    """
    :param n: positive integer
    :return: return a single number from the fibonacci sequence
    """
    if n in (0, 1):
        return n
    return fibonacci_number(n - 1) + fibonacci_number(n - 2)


def fibonacci_sequence_list(total_numbers: int):
    """
    :param total_numbers: positive integer, the first count of numbers from the fibonacci sequence
    :return: list of the first {total_numbers} of the fibonacci numbers
    """
    return [fibonacci_number(n) for n in range(total_numbers)]


def locate(sequence: list, number):
    return sequence.index(number)
