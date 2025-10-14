#obliczanie h
def count_h(index, args):
    return args[index] - args[index - 1]

#oblcizanie lambdy
def count_lambda(index, args):
    return 0 if index==0 else count_h(index, args) / (count_h(index, args) + count_h(index + 1, args))

#iloraz roznicowy, zależność rekurencyjna z wikipedii
def f_diff_q(args, vals):
    return vals[0] if len(args)==1 else (f_diff_q(args[1:], vals[1:]) - f_diff_q(args[:-1], vals[:-1])) / (args[-1] - args[0]) 

#obliczanie d
def count_d(index, args, vals):
    return 0 if index==0 else 6 * f_diff_q(args[(index - 1):(index + 2)], vals[(index - 1):(index + 2)])

#obliczanie drugiej pochodnej w wezlach
def sec_deriv(args, vals):
    n = len(args) - 1

    q = [0 for i in range(n)]                          
    u = [0 for i in range(n)]
    lam = [count_lambda(i, args) for i in range(n)]
    d = [count_d(i, args, vals) for i in range(n)]

    for i in range(1, n):
        p = lam[i] * q[i - 1] + 2
        q[i] = (lam[i] - 1) / p
        u[i] = (d[i] - lam[i] * u[i - 1]) / p

    m = [0 for _ in range(n + 1)]
    m[n - 1] = u[n - 1]

    for i in range(n - 2, 0, -1):
        m[i] = u[i] + q[i] * m[i + 1]

    return m

#wzor na s(x) z wykladu
def func_s(index, args, vals):
    m = sec_deriv(args, vals)
    return lambda x: ((m[index - 1] * (args[index] - x) ** 3) / 6 + (m[index] * (x - args[index - 1]) ** 3) / 6 + (vals[index - 1] - (m[index - 1] * count_h(index, args) ** 2) / 6) * (args[index] - x) + (vals[index] - (m[index] * count_h(index, args) ** 2) / 6) * (x - args[index - 1])) / count_h(index, args)

#funkcja zwracajaca nifs3
def nifs(args, vals):
    def f(x):
        for index in range(1, len(args)):
            if args[index - 1] <= x < args[index]:
                return func_s(index, args, vals)(x)
    return f