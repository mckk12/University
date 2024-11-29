s = input()
t = input()

zeros = s.count('0')
ones = s.count('1')

occurences = 0 
i=0
while i <= (len(s)-len(t)+1):
    if sorted(s[i:i+len(t)]) == sorted(t):
        i+=len(t)
        occurences+=1
    else:
        i+=1
        
    