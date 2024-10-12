import decimal as d


def vat_faktura(lst):
    return sum(lst) * 0.23


def vat_paragon(lst):
    return sum(x * 0.23 for x in lst)


# example causing problems
lista = [0.1, 0.1, 0.1]

print(vat_faktura(lista) == vat_paragon(lista))


# way to fix problem using decimal module

def decimal_faktura(lst):
    s = d.Decimal(0)
    for i in lst:
        s += d.Decimal(str(i))
    s *= d.Decimal('0.23')
    return s

def decimal_paragon(lst):
    s = d.Decimal(0)
    for i in lst:
        s += d.Decimal(str(i)) * d.Decimal('0.23')
    return s


print(decimal_faktura(lista) == decimal_paragon(lista))