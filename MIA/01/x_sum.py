def check_sum(tab, x, y):
    sum = tab[x][y]
    for i in range(1, len(tab)-x):              
        if y-i<0 and y+i>=len(tab[0]):
            continue
        if y-i<0:
            sum += tab[i+x][i+y]
        elif y+i>=len(tab[0]):
            sum += tab[i+x][y-i]
        else:    
            sum += tab[i+x][i+y]
            sum += tab[i+x][y-i]

    for i in range(1, x+1):
        if y-i<0 and y+i>=len(tab[0]):
            continue
        elif y-i<0:
            sum += tab[x-i][i+y]
        elif y+i>=len(tab[0]):
            sum += tab[x-i][y-i]
        else:    
            sum += tab[x-i][i+y]
            sum += tab[x-i][y-i]
            
    return sum



t = int(input())
results = []

for j in range(t):
    n, m = map(int, input().split())
    tab = []
    biggest = 0
    for i in range(n):
        tab.append(list(map(int, input().split())))
    for x in range(n):
        for y in range(m):
            sum = check_sum(tab, x, y)
            if sum > biggest:
                biggest = sum
    results.append(biggest)

for i in results:
    print(i)      