phone_book = {}

entry = input()
while not entry.isdigit():
    name, number = entry.split('-')
    if name not in phone_book:
        phone_book[name] = ''
    phone_book[name] = number
    entry = input()

for _ in range(int(entry)):
    contact = input()
    if contact in phone_book:
        print(f"{contact} -> {phone_book[contact]}")
    else:
        print(f"Contact {contact} does not exist.")
