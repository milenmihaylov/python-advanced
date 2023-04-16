longest_intersection = set()
for _ in range(int(input())):
    first_range, second_range = input().split('-')
    first_start, first_end = first_range.split(',')
    second_start, second_end = second_range.split(',')

    first_range = set()
    for num in range(int(first_start), int(first_end) + 1):
        first_range.add(num)

    second_range = set()
    for num in range(int(second_start), int(second_end) + 1):
        second_range.add(num)

    intersection = first_range & second_range
    if len(intersection) > len(longest_intersection):
        longest_intersection = sorted(intersection)

print(f"Longest intersection is {longest_intersection} with length {len(longest_intersection)}")
