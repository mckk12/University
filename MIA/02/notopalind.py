numbers = map(int, input().split())
n = numbers[0]
p = numbers[1]
word = input()

letters = list(map(chr, range(97, 123)))

allowedLetters = letters[:p]
