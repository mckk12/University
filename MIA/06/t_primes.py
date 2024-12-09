k = int(input())
x = list(map(int, input().split()))

def sieve(n):
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return primes

primes = sieve(int(max(x)**0.5)+1)

for i in x:
    sq = i**0.5
    if int(sq) == sq and primes[int(sq)]:
        print('YES')
    else:
        print('NO') 