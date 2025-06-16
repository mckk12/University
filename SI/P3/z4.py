
def B(i,j):
    return 'B_%d_%d' % (i,j)
    
def domains(Vs):
    return [ q + ' in 0..1' for q in Vs ]

def radars(rows, cols):
    cs = []
    for i in range(len(rows)):
        cs.append('sum([%s], #=, %d)' % (', '.join([B(i,j) for j in range(len(cols))]), rows[i]))
    for j in range(len(cols)):
        cs.append('sum([%s], #=, %d)' % (', '.join([B(i,j) for i in range(len(rows))]), cols[j]))
    return cs

def rectangle2x2(rows, cols):
    cs = []
    for i in range(1, len(rows)-1):
        for j in range(1, len(cols)-1):
            cs.append('%s #==> (%s #\/ %s)' % (B(i,j), B(i-1,j), B(i+1,j)))
            cs.append('%s #==> (%s #\/ %s)' % (B(i,j), B(i,j-1), B(i,j+1)))
    return cs

def no_corners(rows, cols):
    cs = []
    for i in range(len(rows)-1):
        for j in range(len(cols)-1):
            cs.append('(%s #/\ %s) #<==> (%s #/\ %s)' % (B(i,j), B(i+1,j+1), B(i,j+1), B(i+1,j)))
    return cs

def print_constraints(Cs, indent, d):
    position = indent
    writeln (indent * ' ', end='')
    for c in Cs:
        writeln (c + ',', end=' ')
        position += len(c)
        if position > d:
            position = indent
            writeln ('')
            writeln (indent * ' ', end='')

def storms(rows, cols, triples):
    
    R = len(rows)
    C = len(cols)
    
    bs = [ B(i,j) for i in range(R) for j in range(C)]
    
    
    writeln(':- use_module(library(clpfd)).')
    writeln('solve([' + ', '.join(bs) + ']) :- ')
    
    cs = domains(bs) + radars(rows, cols) + rectangle2x2(rows, cols) + no_corners(rows, cols)

    for i,j,val in triples:
        cs.append( '%s #= %d' % (B(i,j), val) )

    print_constraints(cs, 4, 70)
    writeln('')
    writeln('    labeling([ff], [' +  ', '.join(bs) + ']).' )
    writeln('')
    writeln(":- solve(X), write(X), nl.") # tell('prolog_result.txt') - musiałem usunąć

def writeln(s, end="\n"):
    output.write(s + end)

txt = open('zad_input.txt').readlines()
output = open('zad_output.txt', 'w')

rows = list(map(int, txt[0].split()))
cols = list(map(int, txt[1].split()))
triples = []

for i in range(2, len(txt)):
    if txt[i].strip():
        triples.append(map(int, txt[i].split()))

storms(rows, cols, triples)            
        

