n = int(input())
ws = list(map(int, input().split()))
p = int(input())
for _ in range(p):
    a, b = map(int, input().split())
    print(sum(ws[a - 1::b]))
    