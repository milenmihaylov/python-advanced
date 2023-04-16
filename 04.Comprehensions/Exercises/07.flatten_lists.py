text = input().split('|')
print(' '.join([' '.join(text[i].split()) for i in range(-1, -len(text) - 1, -1)]))
