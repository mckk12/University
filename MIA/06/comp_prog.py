n = int(input())
y = []
for i in range(n):
    y.append(input())

def two_divisible(x):
    div = 0
    for j in x:
        if int(j) % 2 == 0:
            div+=1
    if div >= 2:
        return True
    else:
        return False

            
        
for i in y:
    sum = 0
    for j in i:
        sum += int(j)
    if sum % 3 == 0 and '0' in i and two_divisible(i):
        print('red')
    else:
        print('cyan')