characters = {"-", ",", ".", "!", "?"}
with open("text.txt") as file:
    i = 0
    for line in file.readlines():
        if i % 2 == 0:
            word_list = line.split()
            word_list.reverse()
            j = 0
            for word in word_list:
                new_word = ''
                for ch in word:
                    if ch in characters:
                        ch = '@'
                    new_word += ch
                index = word_list.index(word)
                word_list.insert(index, new_word)
                word_list.remove(word)
                j += 1
            print(' '.join(word_list))
        i += 1


