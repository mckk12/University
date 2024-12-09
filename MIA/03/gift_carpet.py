t = int(input())

answers = []


for i in range(t):
    n, m = map(int, input().split())
    words = []
    columns = []
    vika = 'vika '
    for j in range(n):
        words.append(input())
    for j in range(m):
        column = ""
        for k in range(n):
            column+=words[k][j]
        columns.append(column)
    for j in columns:
        if vika[0] in j:
            vika = vika[1:]
            if vika == " ":
                answers.append('YES')
                break
        else:
            continue

    if vika != " ":
        answers.append('NO')

for x in answers: print(x)      
