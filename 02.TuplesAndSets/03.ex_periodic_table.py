periodic_table = set()
for _ in range(int(input())):
    elements = input().split()
    for el in elements:
        periodic_table.add(el)

[print(el) for el in periodic_table]
