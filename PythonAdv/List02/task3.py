def calc_statistics(text, language):
    # polski, angielski i niemiecki
    text = text.replace(' ', '').replace('\n', '').replace('\t', '')
    letters = len(text)
    polish = {x : 0 for x in 'aąbcćdeęfghijklłmnńoóprsśtuwyzźż'}
    english = {x : 0 for x in 'abcdefghijklmnopqrstuvwxyz'}
    german = {x : 0 for x in 'abcdefghijklmnopqrstuvwxyzäöüß'}
    for letter in text:
        if letter.lower() in polish:
            polish[letter.lower()] += 1
        if letter.lower() in english:
            english[letter.lower()] += 1
        if letter.lower() in german:
            german[letter.lower()] += 1
    for key in polish:
        polish[key] /= letters
    for key in english:
        english[key] /= letters
    for key in german:
        german[key] /= letters
    
    if language == 'polish':
        return polish
    elif language == 'english':
        return english
    elif language == 'german':
        return german

