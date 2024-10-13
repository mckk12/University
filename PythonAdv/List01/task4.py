import math
import random as r

# wyliczenie naszego pi
def count_pi(l, c):
    return 4*l/c
# obliczenie odległości od środka
def distance(x, y, mid):
    return math.sqrt((x - mid)**2 + (y - mid)**2)

# liczba trafień wewnątrz okręgu
ltwo = 0
# całkowita liczba trafień w tarczę
cltwt = 0

# przybliżenie pi którego szukamy
pi_range = 0.0001

# dane figur
square = 1000
middle = square / 2
radius = square / 2

# losowanie rzutów i obliczanie pi
ltwo = 0 # liczba trafień wewnątrz okręgu
cltwt = 0 # całkowita liczba trafień w tarczę
my_pi = 0
while not (my_pi - float(pi_range) <= math.pi and my_pi + float(pi_range) >= math.pi):
    x = r.uniform(0, square+1)
    y = r.uniform(0, square+1)
    if distance(x, y, middle) < radius:
        ltwo += 1
    cltwt += 1
    my_pi = count_pi(ltwo, cltwt)
    print(my_pi)
    