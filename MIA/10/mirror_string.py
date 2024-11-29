test = int(input())

for _ in range(test):
    n = int(input())
    s = input().strip()
    k=0
    if len(s) == 1 or s[0] == s[1]:
        print(s[0]*2)
        continue
    while k < n-1 and s[k] >= s[k+1]:
        k+=1

    s = s[:k+1]
    print(s+s[::-1])
    

