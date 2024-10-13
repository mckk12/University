import decimal as dc

def tabliczka(x1, x2, y1, y2, d):
    col_width = max(len(str(x2*y2)), len(str(x1*y1)), len(str(x2*y1)), len(str(x1*y2)), len(str(x1)), len(str(x2)), len(str(y1)), len(str(y2)))+1
    first_col_width = max(len(str(y1)), len(str(y2)))
    print(' ' * first_col_width, end='')
    x = x1
    while x <= x2:
        print((col_width - len(str(x))) * ' ' + str(x), end='')
        x += d
    print()
    while y1 <= y2:
        print((first_col_width - len(str(y1))) * ' ' + str(y1), end='')
        x = x1
        while x <= x2:
            print((col_width - len(str(x * y1))) * ' ' + str(x * y1), end='')
            x += d
        print()
        y1 += d

tabliczka(-1.0, 2.0, 2.0, 10.0, 1.0)