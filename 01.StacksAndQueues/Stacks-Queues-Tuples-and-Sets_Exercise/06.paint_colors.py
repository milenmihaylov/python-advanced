from collections import deque

input_colors = deque(input().split())
main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]
collected_colors = []
subset_collection = []

while input_colors:
    if len(input_colors) > 1:
        new_color = input_colors[0] + input_colors[-1]
    else:
        new_color = input_colors[0]

    if new_color in main_colors:
        collected_colors.append(new_color)
        input_colors.popleft()
        if input_colors:
            input_colors.pop()
    elif new_color in secondary_colors:
        collected_colors.append(new_color)
        subset_collection.append(new_color)
        input_colors.popleft()
        if input_colors:
            input_colors.pop()

    else:
        new_color = input_colors[-1] + input_colors[0]
        if new_color in main_colors:
            collected_colors.append(new_color)
            input_colors.popleft()
            if input_colors:
                input_colors.pop()
            continue
        elif new_color in secondary_colors:
            collected_colors.append(new_color)
            subset_collection.append(new_color)
            input_colors.popleft()
            if input_colors:
                input_colors.pop()
            continue

        new_first_part = input_colors[0][:-1]
        new_second_part = input_colors[-1][:-1]
        if len(new_first_part):
            input_colors.insert(int(len(input_colors)/2), new_first_part)
        if len(new_second_part):
            input_colors.insert(int(len(input_colors) / 2), new_second_part)

        input_colors.popleft()
        if input_colors:
            input_colors.pop()


for color in subset_collection:
    if color == 'orange':
        if 'red' not in collected_colors or 'yellow' not in collected_colors:
            collected_colors.remove(color)
    elif color == 'purple':
        if 'red' not in collected_colors or 'blue' not in collected_colors:
            collected_colors.remove(color)
    elif color == 'green':
        if 'yellow' not in collected_colors or 'blue' not in collected_colors:
            collected_colors.remove(color)


print(collected_colors)
