# # How it is not done:
# print([int(el) for row in [[el for el in input().split(', ')] for _ in range(int(input()))] for el in row])


nums = []
for _ in range(int(input())):
    nums.extend([int(num) for num in input().split(', ')])
print(nums)
