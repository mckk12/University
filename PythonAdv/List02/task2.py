def sudan(n, x, y):
    if n == 0:
        return x + y
    elif y==0:
        return x
    else:
        temp = sudan(n, x, y-1)
        return sudan(n-1, temp, temp + y)
    
def sudan_mem(n, x, y, mem = {}):
    if (n, x ,y) in mem:
        return mem[(n, x, y)]
    if n == 0:
        mem[(n, x, y)] = x + y
        return x + y
    elif y==0:
        mem[(n, x, y)] = x
        return x
    else:
        temp = sudan_mem(n, x, y-1, mem)
        mem[(n, x, y-1)] = temp
        h = sudan_mem(n-1, temp, temp + y, mem)
        mem[(n, x, y)] = h
        return h
    
# print(sudan(2,2,2))
# print(sudan(1,2,997))
# print(sudan_mem(3, 1, 1))
# niezależnie od memoizacji to są najwyzsze wartości jakie udało mi się uzyskać
# wg wikipedi funkcja sudana jest to funkcja rekurencyjna nie prymitywna


