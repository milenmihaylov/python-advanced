bunker = {category: [] for category in input().split(', ')}
count_of_items = 0
count_of_quality = 0
for _ in range(int(input())):
    category, item, quantity_quality = input().split(' - ')
    bunker[category].append(item)
    qnt, qly = quantity_quality.split(';')
    count_of_items += int(qnt.split(':')[1])
    count_of_quality += int(qly.split(':')[1])


print(f"Count of items: {count_of_items}")
print(f"Average quality: {(count_of_quality/len(bunker)):.2f}")
[print(f"{ctgry} -> {', '.join(bunker[ctgry])}") for ctgry in bunker]
