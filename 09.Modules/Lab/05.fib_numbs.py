import fibonacci

nums_list = []
commands = input().split()
while commands[0] != 'Stop':
    if commands[0] == "Create":
        count = int(commands[2])
        nums_list = fibonacci.fibonacci_sequence_list(count)
        print(' '.join([str(el) for el in nums_list]))
    elif commands[0] == "Locate":
        number = int(commands[1])
        try:
            index = fibonacci.locate(nums_list, number)
            print(f"The number - {number} is at index {index}")
        except ValueError:
            print(f"The number {number} is not in the sequence")

    commands = input().split()
