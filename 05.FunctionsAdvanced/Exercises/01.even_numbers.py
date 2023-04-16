nums = [int(x) for x in input().split()]
print([x for x in filter(lambda x: x % 2 == 0, nums)])
