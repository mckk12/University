import random as rd
def uprosc_zdanie(tekst, dl_slowa, liczba_slow):
    slowa = tekst.split()
    nowy_tekst = []

    for slowo in slowa:
        if len(slowo) <= dl_slowa:
            nowy_tekst.append(slowo)
    
    while len(nowy_tekst) > liczba_slow:
        num = rd.randint(1, len(nowy_tekst)-1)
        nowy_tekst.pop(num)

    for i in range(len(nowy_tekst)):
        if (i == len(nowy_tekst)-1):
            print(nowy_tekst[i], end='.')
        else:
            print(nowy_tekst[i], end=' ')
    
tekst = "Podział peryklinalny inicjałów wrzecionowatych kambium charakteryzuje się ścianą podziałową inicjowaną w płaszczyźnie maksymalnej."
uprosc_zdanie(tekst, 10, 5)