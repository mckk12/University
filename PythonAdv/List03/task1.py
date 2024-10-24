import timeit

def pierwsze_imperatywna(n):
    primes = []
    for i in range(2, n):
        is_prime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

def pierwsze_skladana(n):
    return [i for i in range(2, n) if not any(i % j == 0 for j in range(2, int(i**0.5) + 1))]

def pierwsze_funkcyjna(n):
    return list(filter(lambda x: all(x % j != 0 for j in range(2, int(x**0.5) + 1)), range(2, n)))


print(" n\t\tskladana  imperatywna  funkcyjna")
for i in range(1, 6):
    n = 10000 * i
    print(f"{n}:", end="\t\t   ")
    print(f"{timeit.timeit(f'pierwsze_skladana({n})', setup='from __main__ import pierwsze_skladana', number=1):.3f}", end="\t")
    print(f"{timeit.timeit(f'pierwsze_imperatywna({n})', setup='from __main__ import pierwsze_imperatywna', number=1):.3f}", end="\t   ")
    print(f"{timeit.timeit(f'pierwsze_funkcyjna({n})', setup='from __main__ import pierwsze_funkcyjna', number=1):.3f}")