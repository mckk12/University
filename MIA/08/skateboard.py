s = input()

sum = 0
for i in range(len(s)):
    if(int(s[i])%4==0):
        sum+=1
    if(i+1<len(s)):
        if((int(s[i:i+2]))%4==0):
            sum+=1
            sum+=i


print(sum)

