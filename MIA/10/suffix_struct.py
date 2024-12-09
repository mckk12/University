s = input()
t = input()
# array - zamiana dwoch
# automaton - kasowanie elementow

def both(word, word2):
    word = sorted(word)
    word2 = sorted(word2)
    if automaton(word, word2):
        return True
    return False

def automaton(word, word2):
    if word2 in word:
        return True   
    n = 0
    for i in word:
        n += i==word2[n]
        if n == len(word2):
            return True

    return False

if sorted(s) == sorted(t):
    print("array")
    exit()

if automaton(s, t):
    print("automaton")
    exit()

if both(s, t):
    print("both")
    exit()

print("need tree")