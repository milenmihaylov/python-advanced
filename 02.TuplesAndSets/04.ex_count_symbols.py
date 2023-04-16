text = tuple(el for el in input())
unique_el = set()
for el in sorted(text):
    if el not in unique_el:
        print(f"{el}: {text.count(el)} time/s")
        unique_el.add(el)
