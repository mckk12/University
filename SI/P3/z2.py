from copy import deepcopy

class Variable:
    def __init__(self, index, is_row, constraints, length):
        self.index = index
        self.is_row = is_row
        self.constraints = constraints
        self.length = length
        self.domains = self.create_possibilities()

    def create_possibilities(self):
        def generate(seq, constraints):
            if not constraints:
                yield seq + [0] * (self.length - len(seq))
                return
            block_len = constraints[0]
            max_zeros = self.length - sum(constraints) - len(constraints) + 1 - len(seq)
            for zeros in range(max_zeros + 1):
                new_seq = seq + [0] * zeros + [1] * block_len
                if len(new_seq) < self.length:
                    new_seq.append(0)
                yield from generate(new_seq, constraints[1:])

        return [list(x) for x in generate([], self.constraints) if len(x) == self.length]

def set_obvious(drawing, var_rows, var_cols):
    for i in range(len(var_rows)):
        for j in range(len(var_cols)):
            if drawing[i][j] != -1:
                continue
            if all(d[j] == 1 for d in var_rows[i].domains):
                drawing[i][j] = 1
                var_cols[j].domains = [d for d in var_cols[j].domains if d[i] == 1]
            elif all(d[j] == 0 for d in var_rows[i].domains):
                drawing[i][j] = 0
                var_cols[j].domains = [d for d in var_cols[j].domains if d[i] == 0]
            elif all(d[i] == 1 for d in var_cols[j].domains):
                drawing[i][j] = 1
                var_rows[i].domains = [d for d in var_rows[i].domains if d[j] == 1]
            elif all(d[i] == 0 for d in var_cols[j].domains):
                drawing[i][j] = 0
                var_rows[i].domains = [d for d in var_rows[i].domains if d[j] == 0]
    return drawing, var_rows, var_cols

def is_complete(drawing, var_rows, var_cols):
    for row in var_rows:
        blocks = count_blocks(drawing[row.index])
        if blocks != row.constraints:
            return False
    for col in var_cols:
        col_vals = [drawing[r][col.index] for r in range(len(var_rows))]
        blocks = count_blocks(col_vals)
        if blocks != col.constraints:
            return False
    return True

def select_unassigned_variable(drawing, var_rows, var_cols):
    pairs = [(var_rows[i], var_cols[j]) for i in range(len(var_rows)) for j in range(len(var_cols)) if drawing[i][j] == -1]
    if not pairs:
        return None, None
    col_drawing = [list(i) for i in zip(*drawing)]
    res = min(pairs, key=lambda p: len(p[0].domains) + len(p[1].domains) + drawing[p[0].index].count(-1) + col_drawing[p[1].index].count(-1)) # minimize remaining options
    return res

def order(drawing, var_row, var_col):
    ones, zeros = 0, 0
    for d in var_row.domains:
        if d[var_col.index] == 1: ones += 1
        else: zeros += 1
    for d in var_col.domains:
        if d[var_row.index] == 1: ones += 1
        else: zeros += 1
    return [0, 1] if ones >= zeros else [1, 0] # fail-first heuristic

def count_blocks(line):
    blocks = []
    count = 0
    for v in line:
        if v == 1:
            count += 1
        elif count > 0:
            blocks.append(count)
            count = 0
    if count > 0:
        blocks.append(count)
    return blocks

def check_line(line, var):
    for possible in var.domains:
        if all(line[i] == -1 or line[i] == possible[i] for i in range(len(line))):
            return True
    return False

def is_consistent(drawing, var_rows, var_cols):
    for i, row in enumerate(var_rows):
        line = drawing[i]
        if not check_line(line, row):
            return False
    for i, col in enumerate(var_cols):
        col_vals = [drawing[r][i] for r in range(len(var_rows))]
        if not check_line(col_vals, col):
            return False
    return True

def backtrack(drawing, var_rows, var_cols):
    drawing, var_rows, var_cols = set_obvious(drawing, var_rows, var_cols)
    draw_nonogram(drawing)
    if is_complete(drawing, var_rows, var_cols):
        return drawing
    v_row, v_col = select_unassigned_variable(drawing, var_rows, var_cols)
    if not v_row:
        return None
    for val in (order(drawing, v_row, v_col)):
        new_drawing = [row.copy() for row in drawing]
        new_drawing[v_row.index][v_col.index] = val
        if is_consistent(new_drawing, var_rows, var_cols):
            new_rows = deepcopy(var_rows)
            new_cols = deepcopy(var_cols)
            new_rows[v_row.index].domains = [d for d in new_rows[v_row.index].domains if d[v_col.index] == val]
            new_cols[v_col.index].domains = [d for d in new_cols[v_col.index].domains if d[v_row.index] == val]
            result = backtrack(new_drawing, new_rows, new_cols)
            if result is not None:
                return result
    return None

def solve_nonogram(x, y, rows, cols):
    var_rows = [Variable(i, True, rows[i], y) for i in range(x)]
    var_cols = [Variable(i, False, cols[i], x) for i in range(y)]

    drawing = [[-1 for _ in range(y)] for _ in range(x)]
    return backtrack(drawing, var_rows, var_cols)

def draw_nonogram(drawing):
    for row in drawing:
        print(''.join('#' if c == 1 else '.' for c in row))
    print()

def run():
    with open('zad_input.txt') as f:
        data = f.readlines()
    x, y = map(int, data[0].split())
    rows = [list(map(int, line.split())) for line in data[1:x+1]]
    cols = [list(map(int, line.split())) for line in data[x+1:]]

    solution = solve_nonogram(x, y, rows, cols)
    if solution:
        draw_nonogram(solution)
        with open('zad_output.txt', 'w') as f:
            for row in solution:
                f.write(''.join('#' if c == 1 else '.' for c in row) + '\n')
    else:
        print("No solution found.")

if __name__ == '__main__':
    run()
