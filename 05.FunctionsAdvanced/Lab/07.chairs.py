# from itertools import combinations

def print_combinations(list_of_items: list, k: int, combs=[]):
    if len(combs) == k:
        print(', '.join(combs))
        return

    for i in range(len(list_of_items)):
        item = list_of_items[i]
        combs.append(item)
        print_combinations(list_of_items[i + 1:], k, combs)
        combs.pop()


people = input().split(', ')
seats = int(input())

print_combinations(people, seats)

# for combo in combinations(people, seats):
#     print(', '. join([person for person in combo]))
