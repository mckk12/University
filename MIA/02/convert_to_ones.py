
n, x, y = map(int, input().split())
a = input()
h=0
i=0

while i<n:
    j=i
    while(j<n and a[j]==a[i]):
        j+=1
    if(a[i]=='0'):
        h+=1
    i=j


if(h==0):
    print(0)
elif (x<y):
    print((h-1)*x+y)
else:
    print(h*y)

