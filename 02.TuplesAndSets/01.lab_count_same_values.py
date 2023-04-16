numbers = tuple(float(num) for num in input().split())
total_count = 0
counted_numbers = []
for num in numbers:
    if num not in counted_numbers:
        count = numbers.count(num)
        print(f"{num} - {count} times")
        total_count += count
        counted_numbers.append(num)
    else:
        continue
    if total_count == len(numbers):
        break
