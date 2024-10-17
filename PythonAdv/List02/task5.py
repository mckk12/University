def kompresja(tekst):
    curr_lett = tekst[0]
    count = 1
    kompres = []
    for lett in tekst[1:]:
        if lett == curr_lett:
            count+=1
        else:
            kompres.append((count, curr_lett))
            curr_lett = lett
            count = 1
    kompres.append((count, curr_lett))
    return kompres

def dekompresja(tekst_skompresowany):
    tekst = ""
    for (x, y) in tekst_skompresowany:
        tekst += x*y
    return tekst



print(dekompresja(kompresja('suuuuuper')))
                