from collections import deque

food_quantity = int(input())
orders_queue = deque([int(num) for num in input().split()])

print(max(orders_queue))
while orders_queue:
    if orders_queue[0] <= food_quantity:
        food_quantity -= orders_queue.popleft()
    else:
        print(f"Orders left: {' '.join([str(order) for order in orders_queue])}")
        break
else:
    print("Orders complete")
