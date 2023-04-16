with open("output.txt", 'w') as output_file:
    pass
the_dict = {}
with open('words.txt') as open_file:
    for line in open_file:
        for word in line.split():
            word = word.lower()
            the_dict[word] = 0
            with open('text_1.txt') as input_file:
                for input_line in input_file.readlines():
                    count = input_line.lower().split().count(word)
                    the_dict[word] += count


output_file = open("output.txt", 'a')
for key, value in sorted(the_dict.items(), key=lambda x: -x[1]):
    output_file.write(f"{key} - {value}\n")

output_file.close()
