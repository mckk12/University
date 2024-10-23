# lista rozwiazan, rozwiazanie = lista 4 list dlugosci 4 zawierajacych informacje o kazdym wierszy
def cienie(v1, v2):
    h1 = list(v1)
    h2 = list(v2)
    rozwiazanie = [[0 for i in range(4)] for j in range(4)]
    for j in range(len(h1)):
        if h1[j] > 0:
            for i in range(len(h2)):
                if h2[i] > 0:
                    h1[j] -= 1
                    while h1[j] > 0:
                        rozwiazanie[i][j] = 1
                        i += 1
                        h2[i] -= 1
                    break
                if 
            


    return 



def wyswietl_rozw(rozw):
    for i in range(4):
        for j in range(4):
            print("X", end=" ") if rozw[i][j] else print("O", end=" ")
        print()
    return

zadanie = cienie((2,1,3,1), (1,3,1,2))

for rozwiazanie in zadanie:
    wyswietl_rozw(rozwiazanie)


