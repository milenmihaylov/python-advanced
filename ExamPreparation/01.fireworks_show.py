from collections import deque


def check_zero_value(queue: deque = None, stack: list = None):
    while queue:
        if queue[0] <= 0:
            queue.popleft()
        else:
            break
    while stack:
        if stack[-1] <= 0:
            stack.pop()
        else:
            break


def check_empty_sequences(queue: deque = None, stack: list = None):
    if len(queue) == 0:
        return True
    if len(stack) == 0:
        return True
    return False


def enough_fireworks(palm: int, willow: int, crossette: int):
    if palm >= 3 and willow >= 3 and crossette >= 3:
        return True
    return False


fireworks_effects = deque([int(x) for x in input().split(', ')])
explosive_powers = [int(x) for x in input().split(', ')]

palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
good_fireworks = False

while fireworks_effects and explosive_powers:
    check_zero_value(queue=fireworks_effects, stack=explosive_powers)
    if check_empty_sequences(fireworks_effects, explosive_powers):
        break
    current_firework_effect = fireworks_effects.popleft()
    current_explosive_power = explosive_powers.pop()
    sum_mix = current_firework_effect + current_explosive_power
    if sum_mix % 3 == 0 and sum_mix % 5 != 0:
        palm_fireworks += 1
    elif sum_mix % 5 == 0 and sum_mix % 3 != 0:
        willow_fireworks += 1
    elif sum_mix % 3 == 0 and sum_mix % 5 == 0:
        crossette_fireworks += 1
    else:
        current_firework_effect -= 1
        fireworks_effects.append(current_firework_effect)
        explosive_powers.append(current_explosive_power)

    if enough_fireworks(palm_fireworks, willow_fireworks, crossette_fireworks):
        good_fireworks = True
        break

if good_fireworks:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")
if fireworks_effects:
    print(f"Firework Effects left: {', '.join([str(x) for x in fireworks_effects])}")
if explosive_powers:
    print(f"Explosive Power left: {', '.join([str(x) for x in explosive_powers])}")
print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
