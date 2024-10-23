from itertools import product

# tworzymy wszystkie mozliwosci wypelnienia kolumn -> obliczamy iloczyn kartezjanski -> filtrujemy po wartosciach na wierszach
def cienie(v1, v2):
    wymiar = len(v1)
    opcje = filter(
        lambda x: all(
            sum(x[i][j] for i in range(wymiar)) == v2[j] 
            and ''.join('1'*v2[j]) in ''.join(map(str, (x[i][j] for i in range(wymiar)))) 
            for j in range(wymiar)
        ) ,
        product(
            *(
                [
                    [0] * j + [1] * v1[i] + [0] * (wymiar - v1[i] - j)
                    for j in range(wymiar - v1[i] + 1)
                ]
                for i in range(wymiar)
            )
        )
    )
    # print(list(opcje))
    return opcje



# i oraz j odwrotnie poniewaz chcemy po kolumnach iterowac
def wyswietl_rozw(rozw):
    wymiar = len(list(rozw))
    for j in range(wymiar):
        for i in range(wymiar):
            print("X", end=" ") if rozw[i][j] else print("O", end=" ")
        print()
    return


zadanie = cienie((2,1,3,1), (1,3,1,2))


for rozwiazanie in zadanie:
    wyswietl_rozw(rozwiazanie)
    print()


