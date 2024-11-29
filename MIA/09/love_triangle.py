n = int(input())
f = list(map(int, input().split()))

f = [0] + f

for i in f:
    if f[f[f[i]]] == i and i != f[i]:
        print("YES")
        exit()
print("NO")