kids = input().split()
n_toss = int(input())
index = -1
count = 0
while len(kids) > 1:
    while count < n_toss:
        count += 1
        index += 1
        if index == len(kids):
            index = 0
    removed_kid = kids.pop(index)
    index -= 1
    print(f"Removed {removed_kid}")
    count = 0

print(f"Last is {kids[0]}")
