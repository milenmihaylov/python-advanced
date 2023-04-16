heroes_inventory = {hero: {'items': [], 'costs': 0} for hero in input().split(', ')}
items = input()
while not items == 'End':
    hero_name, item_name, item_cost = items.split('-')

    if item_name not in heroes_inventory[hero_name]['items']:
        heroes_inventory[hero_name]['items'].append(item_name)
        heroes_inventory[hero_name]['costs'] += int(item_cost)
    items = input()

[print(f"{hero} -> Items: {len(item['items'])}, Cost: {item['costs']}") for hero, item in heroes_inventory.items()]
