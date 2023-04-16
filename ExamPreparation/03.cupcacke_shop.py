from collections import deque


def stock_availability(inventory_list: deque, delivery_sell: str, *args):
    inventory = deque(inventory_list)
    if delivery_sell == 'delivery':
        inventory.extend(args)
    elif delivery_sell == 'sell':
        if len(args) == 0:
            inventory.popleft()
        else:
            for el in args:
                if isinstance(el, int):
                    for _ in range(int(el)):
                        inventory.popleft()
                    # break
                elif isinstance(el, str):
                    while el in inventory:
                        inventory.remove(el)
    return list(inventory)


print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
