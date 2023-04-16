punct_marks = ("-", ",", ".", "!", "?", "'")
i = 0
file = open("text.txt")
output_file = open("output.txt", 'w')
for line in file.readlines():
    i += 1
    count_letters = 0
    count_punct_marks = 0
    for ch in line:
        if ch in punct_marks:
            count_punct_marks += 1
        elif ch != ' ' and ch != '\n':
            count_letters += 1
    output_file.write(f"Line {i}: {line[:-1]} ({count_letters})({count_punct_marks})\n")
