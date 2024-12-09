n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

for i in a:
    if i < 0:
        print(i)
        break
    elif (i**0.5) % 1 != 0:
        print(i)
        break