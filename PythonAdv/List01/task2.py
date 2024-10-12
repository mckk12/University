import string

def is_palindrome(word):
    word = word.translate({ord(i): None for i in string.punctuation+' '}).lower()
    return word == word[::-1]

print(is_palindrome("Eine güldne, gute Tugend: Lüge nie!"))
print(is_palindrome("Míč omočím."))