n = int(input())
a = list(map(int, input().split()))

def fn(x):
    return x%(10**9+7)
a = list(map(fn, a))

good_subs = []
sub = []
for i in range(len(a)):
    for j in range(i, len(a)):
        sub.append(a[i:j+1])
print(sub)


for i in sub:
    for j in range(len(i)):
        if (i[j] % (j+1)) != 0:
            break
            