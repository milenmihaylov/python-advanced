# def permutations(text, n=0):
#     if n == len(text):
#         print(''.join(text))
#         return
#
#     for i in range(n, len(text)):
#         text[i], text[n] = text[n], text[i]
#         permutations(text, n + 1)
#         text[i], text[n] = text[n], text[i]
from itertools import permutations

text = list(input())
# permutations(text)
[print(''.join(el)) for el in permutations(text)]
