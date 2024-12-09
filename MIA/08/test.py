def silnia(n):
    if n == 0:
        return 1
    return n * silnia(n - 1)
x = 0
suma = 1
while (suma > 10**(-12)):
    suma = 1 / (silnia(x+1) * 2**(2*x+1))
    x+=1

print(suma, x)