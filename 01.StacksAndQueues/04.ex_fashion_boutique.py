clothes_box = [int(x) for x in input().split()]
capacity_of_one_rack = int(input())

current_rack = 0
total_racks = 1
while clothes_box:
    current_clothing = clothes_box.pop()
    if current_rack + current_clothing <= capacity_of_one_rack:
        current_rack += current_clothing
    else:
        total_racks += 1
        current_rack = current_clothing

print(total_racks)
