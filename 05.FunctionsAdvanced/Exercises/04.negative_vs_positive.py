def negatives_sum(numbers):
    return sum(filter(lambda x: x < 0, numbers))


def positives_sum(numbers: list):
    return sum(filter(lambda x: x > 0, numbers))


def comparison_func(negative_sum: int, positive_sum: int):
    if abs(negative_sum) > positive_sum:
        return "The negatives are stronger than the positives"
    else:
        return "The positives are stronger than the negatives"


nums = [int(x) for x in input().split()]
n_sum = negatives_sum(nums)
p_sum = positives_sum(nums)
print(n_sum)
print(p_sum)
print(comparison_func(n_sum, p_sum))
