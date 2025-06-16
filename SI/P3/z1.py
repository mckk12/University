class Variable:
    def __init__(self, index, is_row: bool, constraints, length):
        self.index = index
        self.is_row = is_row
        self.constraints = constraints
        self.length = length
        self.domains = self.create_possiblities()
        # print(self.domains)

    def create_possiblities(self):
        def generate(seq, constraints):
            if not constraints:
                return [seq + [0] * (self.length - len(seq))]
            results = []
            block_len = constraints[0]
            max_zeros = self.length - sum(constraints) - len(constraints) + 1 - len(seq)
            for zeros in range(max_zeros + 1):
                new_seq = seq + [0] * zeros + [1] * block_len
                if len(new_seq) < self.length:
                    new_seq.append(0) 
                results.extend(generate(new_seq, constraints[1:]))
            return results

        return [''.join(map(str, x)) for x in generate([], self.constraints) if len(x) == self.length]

            
        
def reduce(var_i, var_j):
    revised = False
    domain_i = var_i.domains.copy()
    for x in domain_i:
        if not any(x[var_j.index] == y[var_i.index] for y in var_j.domains):
            var_i.domains.remove(x)
            revised = True
    return revised

def ac3(x, y, var_rows, var_cols):
    worklist = []
    for i in range(x):
        for j in range(y):
            worklist.append((var_rows[i], var_cols[j]))
            worklist.append((var_cols[j], var_rows[i]))
            
    while worklist:
        var_i, var_j = worklist.pop(0)
        if reduce(var_i, var_j):
            if not var_i.domains:
                return False
            neighbors = var_cols if var_i.is_row else var_rows
            for var_k in neighbors:
                if var_k != var_j:
                    worklist.append((var_k, var_i))
                    worklist.append((var_i, var_k))
    return True


def solve_nanogram(x,y,rows,cols):
    drawing = [[0 for _ in range(y)] for _ in range(x)]
    var_rows = [Variable(i, True, rows[i], y) for i in range(x)]
    var_cols = [Variable(i, False, cols[i], x) for i in range(y)]
    if ac3(x, y, var_rows, var_cols):
        for i in range(x):
            # print(var_rows[i].domains)
            drawing[i] = var_rows[i].domains[0]
    # print(drawing)
    return drawing


def draw_nonogram(drawing):
    for row in drawing:
        # print(row.replace("0", ".").replace("1", "#"))
        print("".join(map(str, row)).replace("0", ".").replace("1", "#"))

def run():
    f = open('zad_input.txt', 'r')
    o = 'zad_output.txt'

    data = f.readlines()
    f.close()
    # x w doł, y w prawo
    x, y = map(int, data[0].strip().split())
    rows, cols = [], []
    for line in data[1:x+1]:
        rows.append(list(map(int, (line.strip().split()))))
    for line in data[x+1:]:
        cols.append(list(map(int, (line.strip().split()))))
    # print(x, y, rows, cols)

    answer = solve_nanogram(x, y, rows, cols)
    draw_nonogram(answer)

    with open(o, 'w') as o:
        for row in answer:
            # o.write(row.replace("0", ".").replace("1", "#") + '\n')
            o.write("".join(map(str, row)).replace("0", ".").replace("1", "#") + '\n')

if __name__ == '__main__':
    run()
    # pass