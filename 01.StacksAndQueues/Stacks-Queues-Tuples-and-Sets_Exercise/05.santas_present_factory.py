from collections import deque


def build_present(total):
    for gift, magic_needed in presents.items():
        if total == magic_needed:
            crafted.append(gift)
            return True
    return False


materials = [int(x) for x in input().split()]
magic_values = deque([int(x) for x in input().split()])

presents = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400}

crafted = []
success = False

while materials and magic_values:
    box_of_materials = materials.pop()
    magic_level = magic_values.popleft()
    total_magic_value = box_of_materials * magic_level
    if build_present(total_magic_value):
        continue
    if total_magic_value < 0:
        total_magic_value = box_of_materials + magic_level
        materials.append(total_magic_value)
    elif total_magic_value > 0:
        materials.append(box_of_materials + 15)
    else:
        if box_of_materials != 0 and magic_level == 0:
            materials.append(box_of_materials)
        elif box_of_materials == 0 and magic_level != 0:
            magic_values.appendleft(magic_level)

if ("Doll" in crafted and "Wooden train" in crafted) or ("Teddy bear" in crafted and "Bicycle" in crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    materials.reverse()
    print(f"Materials left: {', '.join([str(x) for x in materials])}")
if magic_values:
    print(f"Magic left: {', '.join([str(x) for x in magic_values])}")
crafted_dict = {p: crafted.count(p) for p in crafted}
[print(f"{key}: {value}") for key, value in sorted(crafted_dict.items(), key=lambda x: x[0])]
