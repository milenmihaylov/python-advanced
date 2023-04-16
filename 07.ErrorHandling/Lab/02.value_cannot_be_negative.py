class ValueCannotBeNegative(Exception):
    pass


try:
    numbers = [1, 2, -3, 6, 10]
    for i in range(len(numbers)):
        num = numbers[i + 1]
        if num < 0:
            raise ValueCannotBeNegative
        print('No exception')
except (ValueCannotBeNegative, IndexError) as err:
    print(f"Exception handled: {err}")

