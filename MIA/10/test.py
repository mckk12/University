def litery(word):
    return {i:word.count(i) for i in word}


print(litery("aandinaiwns") == litery("wandinaiwns"))