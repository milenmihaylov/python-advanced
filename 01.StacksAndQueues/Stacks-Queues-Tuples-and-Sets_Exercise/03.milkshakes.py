from collections import deque

chocolates = [int(c) for c in input().split(', ')]
cups_of_milk = deque([int(c) for c in input().split(', ')])

milkshakes = 0

while chocolates and cups_of_milk and milkshakes < 5:
    choco = chocolates.pop()
    cup = cups_of_milk.popleft()

    if choco <= 0 and cup <= 0:
        continue
    if choco <= 0:
        cups_of_milk.appendleft(cup)
        continue
    if cup <= 0:
        chocolates.append(choco)
        continue

    if choco == cup:
        milkshakes += 1

    else:
        cups_of_milk.append(cup)
        chocolates.append(choco - 5)


if milkshakes >= 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(c) for c in chocolates])}")
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk: {', '.join([str(c) for c in cups_of_milk])}")
else:
    print("Milk: empty")
