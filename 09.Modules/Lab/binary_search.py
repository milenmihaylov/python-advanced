import random
from time import time


def binary_search(sequence, number, start_index, end_index):
    mid = (start_index + end_index) // 2
    if number == sequence[mid]:
        return mid
    elif number > sequence[mid]:
        return binary_search(sequence, number, mid + 1, end_index)
    else:
        return binary_search(sequence, number, start_index, mid)


def binary_search_2(sequence, number):
    mid = len(sequence) // 2
    if number == sequence[mid]:
        return mid
    elif number > sequence[mid]:
        return binary_search_2(sequence[mid + 1:], number)
    else:
        return binary_search_2(sequence[:mid], number)


def measure(action, repeat_count=1):
    start_time = time()
    for i in range(repeat_count):
        action()
    end_time = time()
    print(f"-- Executed in {end_time - start_time} seconds")


def find_all(values):
    s = 0
    for val in values:
        s += binary_search(values, val, 0, len(values))
    return s


def find_all_2(values):
    s = 0
    for val in values:
        s += binary_search_2(values, val)
    return s


values = range(2 ** 20)
my_choice = random.choice(values)
print(my_choice)

measure(lambda: find_all(values))
measure(lambda: find_all_2(values))
