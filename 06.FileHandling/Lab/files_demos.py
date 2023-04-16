def write_to_file(file_path, mode, text):
    with open(file_path, mode) as file:
        file.write(text)


write_to_file("words.txt", 'w', 'quick is fault')
