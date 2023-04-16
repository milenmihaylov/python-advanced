# def palindrome(word, index=0):  # without recursion
#     for i in range(len(word)//2):
#         if word[i] == word[i*(-1) -1]:
#             continue
#         else:
#             return f"{word} is not a palindrome"
#     return f"{word} is a palindrome"

def palindrome(word, index=0):
    if index >= int(len(word) / 2):
        return f"{word} is a palindrome"
    if word[index] != word[index * (-1) - 1]:
        return f"{word} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("patezap", 0))
print(palindrome("peter", 0))
print(palindrome("abcfdba", 0))
print(palindrome("abcba", 0))
