def create_file(path_name, mode='w', text=''):
    with open(path_name, mode) as file:
        file.write(text)


create_file("my_first_file.txt",
            text='I just created my first file!')
