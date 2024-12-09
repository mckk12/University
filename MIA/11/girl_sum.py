n, q = map(int, input().split())
a = list(map(int, input().split()))
help = [0] * (n + 1)

for _ in range(q):
    l, r = map(int, input().split())
    help[l-1] += 1
    help[r] -= 1

for i in range(1, n):
    help[i] += help[i-1]


a.sort(reverse=True)
help.sort(reverse=True)

answer = sum(a[i] * help[i] for i in range(n))
print(answer)
