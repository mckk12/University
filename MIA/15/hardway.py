t = int(input())

for _ in range(t):
    xs=[]
    ys=[]
    ans = 0
    for i in range(3):
        x, y = map(int, input().split())
        xs.append(x)
        ys.append(y)
    if ys.count(max(ys)) == 2:
        xs.remove(xs[ys.index(min(ys))])
        ans = abs(xs[0]-xs[1])

    print(ans)
