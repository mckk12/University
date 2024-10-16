from collections import defaultdict as dd

def wyniki_dHondta(wybory, liczba_mandatow):
    wszystkie_glosy = sum(wybory.values())
    prog_wyborczy = 0.05
    wyniki = {komitet: 0 for komitet in wybory}
    i = 1
    ilorazy = dd(list)

    #pętla licząca ilorazy z glosow dopoki nie zapelnimy wszystkich mandatow
    while sum(wyniki.values()) < liczba_mandatow:
        for komitet, glosy in wybory.items(): 
            if glosy < wszystkie_glosy * prog_wyborczy:
                continue

            ilorazy[glosy/(i)].append(komitet)
        
        najwiekszy_iloraz = max(ilorazy)
        wyniki[ilorazy[najwiekszy_iloraz][0]] += 1

        if len(ilorazy[najwiekszy_iloraz]) == 1:
            ilorazy.pop(najwiekszy_iloraz)
        else:
            ilorazy[najwiekszy_iloraz].pop(0)
        i += 1

    return wyniki

wyb = {'A': 720, 'B': 300, 'C': 480}

print(wyniki_dHondta(wyb, 8))

