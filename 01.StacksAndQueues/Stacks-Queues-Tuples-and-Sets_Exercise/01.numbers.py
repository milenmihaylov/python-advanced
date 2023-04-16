def add(sequence: set, nums: set):
    return sequence | nums


def remove(sequence: set, nums: set):
    return sequence - nums


def sub_set(first_set: set, second_set: set):
    if first_set <= second_set or second_set <= first_set:
        return True
    return False


first_line = {int(x) for x in input().split()}
second_line = {int(x) for x in input().split()}

for _ in range(int(input())):
    commands = input().split()
    command = commands[0]
    if commands[0] == "Check":
        print(sub_set(first_set=first_line, second_set=second_line))
        continue
    line = commands[1]
    numbers = {int(num) for num in commands[2:]}
    if command == "Add":
        if line == "First":
            first_line = add(first_line, numbers)
        elif line == "Second":
            second_line = add(second_line, numbers)
    elif command == "Remove":
        if line == "First":
            first_line = remove(first_line, numbers)
        elif line == "Second":
            second_line = remove(second_line, numbers)

print(', '.join([str(el) for el in sorted(first_line)]))
print(', '.join([str(el) for el in sorted(second_line)]))
