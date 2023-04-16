from collections import deque
from functools import reduce


def check_nectar(bee: int):
    if not nectar:
        return False
    last_nectar = nectar.pop()
    if last_nectar >= bee:
        return last_nectar
    return check_nectar(bee)


bees = deque([int(bee) for bee in input().split()])
nectar = [int(n) for n in input().split()]
honey_making_symbols = deque(input().split())

total_honey = 0

operations = {
    "+": lambda a, b: a + b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "-": lambda a, b: a - b
}

while bees and nectar:
    working_bee = bees.popleft()
    matched_nectar = check_nectar(working_bee)
    if not matched_nectar:
        if working_bee != 0:
            bees.appendleft(working_bee)
        continue
    operation_symbol = honey_making_symbols.popleft()
    total_honey += abs(reduce(operations[operation_symbol], (working_bee, matched_nectar)))


print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join([str(b) for b in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(n) for n in nectar])}")
