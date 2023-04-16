def create_file(file):
    f = open(file, 'w')
    f.close()


def add_content(file, content):
    with open(file, 'a') as f:
        f.write(content + '\n')


def replace_content(file, old, new):
    try:
        with open(file) as f:
            s = f.read()
            if old not in s:
                print("An error occurred")
                return

        with open(file, 'w') as f:
            s = s.replace(old, new)
            f.write(s)
    except FileNotFoundError:
        print("An error occurred")


def delete_file(file):
    import os
    if os.path.exists(file):
        os.remove(file)
    else:
        print("An error occurred")


command = input()
while not command == "End":
    command = command.split('-')
    cmd = command[0]
    file_name = command[1]
    if cmd == 'Create':
        create_file(file_name)
    elif cmd == 'Add':
        file_content = command[2]
        add_content(file_name, file_content)
    elif cmd == 'Replace':
        old_string = command[2]
        new_string = command[3]
        replace_content(file_name, old_string, new_string)
    elif cmd == 'Delete':
        delete_file(file_name)

    command = input()
