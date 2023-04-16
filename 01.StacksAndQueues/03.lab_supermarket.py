from collections import deque

queue = deque([])
customer = input()
while not customer == 'End':
    if customer == 'Paid':
        for _ in range(len(queue)):
            print(queue.popleft())
    else:
        queue.append(customer)

    customer = input()

print(f"{len(queue)} people remaining.")
