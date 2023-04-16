from collections import deque

kids = deque(input().split())
n_toss = int(input())

while len(kids) > 1:
    kids.rotate(-n_toss)
    print(f"Removed {kids.pop()}")

print(f"Last is {kids[0]}")
