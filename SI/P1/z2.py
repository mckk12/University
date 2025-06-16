'''
For every letter in a row, we are checking the lenght of every possible word starting from it, that is created from the next letters and is on the list.
Then using dynamic programming we remember the best score (calculated from squared sum of lenghts of words) 
for every position in the text and the position of the last word that was used to get that score.
So that we can be sure all letters are used and we can reconstruct the text.
'''

def read_words(file):
    words = set()
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            words.add(line.strip())
    return words

def reconstruct_text(words, text):
    n = len(text)
    dp = [0] * (n + 1)
    cut = [-1] * (n + 1)

    for i in range(n):
        if dp[i] == 0 and i != 0:
            continue
        for j in range(i + 1, n + 1):
            word = text[i:j]
            if word in words:
                score = len(word) ** 2
                if dp[j] < dp[i] + score:
                    dp[j] = dp[i] + score
                    cut[j] = i

    if dp[n] == 0:
        return "No solution"

    result = []
    i = n
    while i > 0:
        result.append(text[cut[i]:i])
        i = cut[i]
    result.reverse()
    return ' '.join(result)


if __name__ == "__main__":
    words = read_words("words_for_ai1.txt")
    # text = "tamatematykapustkinieznosi"
    # print(reconstruct_text(words, text))

    # pan_tadeusz = open("pan_tadeusz_bez_spacji.txt", "r", encoding="utf-8")
    # for line in pan_tadeusz.readlines():
    #     print(reconstruct_text(words, line.strip()))

    f = open("zad2_input.txt", "r", encoding="utf-8")
    o = open("zad2_output.txt", "w", encoding="utf-8")
    for line in f.readlines():
        o.write(reconstruct_text(words, line.strip()) + "\n")
    f.close()
    o.close()