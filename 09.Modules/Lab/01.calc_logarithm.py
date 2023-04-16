from math import log


def calc_log(number, base):
    if base == "natural":
        return log(number)
    return log(number, int(base))


num = int(input())
base = input()
print(calc_log(num, base))
