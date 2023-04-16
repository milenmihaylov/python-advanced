bunker = {category: {"items": [], "total_quantity": 0, 'total_quality': 0} for category in input().split(', ')}
n = int(input())
for _ in range(n):
    category, item, quantity_quality = input().split(' - ')
    quantity, quality = quantity_quality.split(';')
    qnt = quantity.partition(':')[2]
    qly = quality.partition(':')[2]
    bunker[category]['items'].append(item)
    bunker[category]['total_quantity'] += int(qnt)
    bunker[category]['total_quality'] += int(qly)

count_of_items = 0
count_of_quality = 0
for ctgry, value in bunker.items():
    count_of_items += bunker[ctgry]['total_quantity']
    count_of_quality += bunker[ctgry]['total_quality']

print(f"Count of items: {count_of_items}")
print(f"Average quality: {(count_of_quality/len(bunker)):.2f}")
for ctgry in bunker:
    print(f"{ctgry} -> {', '.join(bunker[ctgry]['items'])}")
