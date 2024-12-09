q = int(input())
answers = []
for _ in range(q):
    s = input()
    t = input()
    a = len(s)
    if list(set(t)) == ['a'] and len(t) == 1:
        answers.append(1)
        continue
    elif('a' in t):
        answers.append(-1)
        continue
    else:
        sum = 2**a
        answers.append(sum)

for i in answers:
    print(i)
