n, a, b = map(int, input().split())
seats = list(x for x in input())

numberOfSitted = 0
for i in range(n):
    if a==0 and b==0:
        break
    if seats[i] == "*":  
        continue
    else: 
        if a > b and seats[i-1] != "A" and a!=0:
            seats[i] = "A"  
            a -= 1
        elif seats[i-1] != "B" and b!=0:
            seats[i] = "B" 
            b -= 1
        elif seats[i-1] == "A" and b!=0:
            seats[i] = "B" 
            b -= 1
        elif seats[i-1] == "B" and a!=0:
            seats[i] = "A" 
            a -= 1
        else:
            continue
        numberOfSitted += 1

print(numberOfSitted)
