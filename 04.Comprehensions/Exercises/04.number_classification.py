numbers = [int(num) for num in input().split(', ')]
positives = []
negatives = []
odds = []
evens = []
[positives.append(str(num)) if num >= 0 else negatives.append(str(num)) for num in numbers]
[evens.append(str(num)) if num % 2 == 0 else odds.append(str(num)) for num in numbers]
print(f'Positive: {", ".join(positives)}')
print(f'Negative: {", ".join(negatives)}')
print(f'Even: {", ".join(evens)}')
print(f'Odd: {", ".join(odds)}')
# for num in numbers:
#     if num >= 0:
#         positives.append(num)
#     else:
#         negatives.append(num)
#     if num % 2 == 0:
#         evens.append(num)
#     else:
#         odds.append(num)