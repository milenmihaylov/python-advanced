def filter_func(number):
    for divider in range(2, 10 + 1):
        if number % divider == 0:
            return True
    return False


start_int = int(input())
end_int = int(input())

print([num for num in range(start_int, end_int + 1) if filter_func(num)])
