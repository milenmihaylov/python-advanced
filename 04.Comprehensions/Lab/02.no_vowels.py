def is_vowel(character):
    return True if character.lower() in 'aouei' else False


print(''.join([letter for letter in input() if not is_vowel(letter)]))
