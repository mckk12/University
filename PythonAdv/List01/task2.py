import string

def is_palindrome(word):
    word = word.strip(string.punctuation+' ').lower()
    print(word.strip(string.punctuation+' ').lower())
    return word == word[::-1]

print(is_palindrome("Eine güldne, gute Tugend: Lüge nie!"))
print(is_palindrome("Míč omočím."))