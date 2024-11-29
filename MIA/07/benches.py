n = int(input())

sum=1

for i in range(5):
    sum*=(n-i)**2

print(int(sum//120))