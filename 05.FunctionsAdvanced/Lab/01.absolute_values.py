# print([abs(float(num)) for num in input().split()])  # easy way


# not easy way
def convert_iter_to_abs(iter):
    return list(map(abs, iter))


nums = map(float, input().split())
print(convert_iter_to_abs(nums))
