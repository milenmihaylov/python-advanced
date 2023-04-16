def odds(numbers: list):
    return sum(filter(lambda x: x % 2 != 0, numbers)) * len(numbers)


def evens(numbers: list):
    return sum(filter(lambda x: x % 2 == 0, numbers)) * len(numbers)


command = input()
nums = [int(x) for x in input().split()]
if command == 'Odd':
    print(odds(nums))
elif command == 'Even':
    print(evens(nums))
