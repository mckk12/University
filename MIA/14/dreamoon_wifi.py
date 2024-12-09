s1 = input()
s2 = input()

diff = s1.count('+') - s1.count('-') - s2.count('+') + s2.count('-')
q_marks = s2.count('?')
pos_guess = 0

for i in range(2**q_marks):
    c, k = diff, i
    for j in range(1, q_marks+1):
        c += 1 if k & 1 else -1
        k //= 2
    pos_guess += 1 if c == 0 else 0


print("{:.20f}".format(pos_guess / 2**q_marks))