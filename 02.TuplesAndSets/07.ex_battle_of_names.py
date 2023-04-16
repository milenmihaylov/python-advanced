odd_set = set()
even_set = set()
for i in range(1, int(input()) + 1):
    name = input()
    ch_sum = 0
    for ch in name:
        ch_sum += ord(ch)
    result = ch_sum // i
    if not result % 2 == 0:
        odd_set.add(result)
    else:
        even_set.add(result)

odd_sum = sum(odd_set)
even_sum = sum(even_set)
if odd_sum == even_sum:
    print(', '.join({str(x) for x in odd_set & even_set}))
elif odd_sum > even_sum:
    print(', '.join({str(x) for x in odd_set - even_set}))
elif odd_sum < even_sum:
    print(', '.join({str(x) for x in odd_set.symmetric_difference(even_set)}))
