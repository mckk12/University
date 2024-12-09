n, m, l = map(int, input().split()) 

hairlines = list(map(int, input().split()))

swings = 0

if hairlines[0]>l:
    swings += 1
for i in range(1, len(hairlines)):
    if hairlines[i]>l and hairlines[i-1]<=l:
        swings += 1
        

for _ in range(m):
    inpt = input().split()
    t = int(inpt[0])
    if t!=0:
        p,d = map(int, inpt[1:])
        if hairlines[p-1]>l:
            hairlines[p-1] += d
            continue
        hairlines[p-1] += d
        if p==1:
            if hairlines[0]>l and (p == n or hairlines[1]<=l):
                swings += 1
        elif p==n:
            if hairlines[n-1]>l and hairlines[n-2]<=l:
                swings += 1
        else:
            if hairlines[p-2]>l and hairlines[p]>l and hairlines[p-1]>l:
                swings -= 1
            if hairlines[p-2]<=l and hairlines[p]<=l and hairlines[p-1]>l:
                swings += 1
    else:
        print(swings)
    