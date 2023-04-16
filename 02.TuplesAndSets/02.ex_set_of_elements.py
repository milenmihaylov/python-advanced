n, m = input().split()
first_set = set()
for _ in range(int(n)):
    first_set.add(input())

second_set = set()
for _ in range(int(m)):
    second_set.add(input())

[print(num) for num in first_set & second_set]
