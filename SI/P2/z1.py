'''
It works the same as the previous version based on WalkSat algorithm, with a change to the error function.
Now instead of just counting amount of changes needed to fix the line we need to take into account more numbers used to define this line.
Idea is that we divide the line into parts that are defined by the numbers in the sequence and then we try to find the best place to switch the pixels.
After calculating the "optimal" solution, we calculate the error it generetes.
'''

import random

def opt_dist_single(seq, num):
    changes = len(seq) + 1
    idx = 0
    for i in range(len(seq) - num + 1):
        curr = seq[i:i+num]
        rest = seq[:i] + seq[i+num:]
        if (curr.count(0) + rest.count(1)< changes):
            changes = curr.count(0) + rest.count(1)
            idx = i
    return changes, idx

def opt_dist(line, sequence):
    optimal = [0 for _ in range(len(line))]
    start = 0
    for i, s in enumerate(sequence):

        end = len(line) - len(sequence[i+1:]) - sum(sequence[i+1:])
        frac_line = line[start:end]
        start += opt_dist_single(frac_line, s)[1]
        
        for j in range(start, start + s):
            optimal[j] = 1
        start += s + 1

    changes = sum([1 for i in range(len(line)) if line[i] != optimal[i]])

    return changes

def switch_pixel(drawing, row, col):
    drawing[row][col] = 0 if drawing[row][col] else 1

def reset_drawing(x, y):
    return [[random.randint(0,1) for _ in range(y)] for _ in range(x)]

def after_switch(drawing, row, col, rows, cols):
    temp_draw = []
    for i in range(len(drawing)):
        temp_draw.append(drawing[i].copy())
    switch_pixel(temp_draw, row, col)
    return opt_dist(temp_draw[row], rows[row]) + opt_dist([temp_draw[x][col] for x in range(len(rows))], cols[col])

def check_correctness(rows, cols, drawing):
    for i in range(len(rows)):
        if opt_dist(drawing[i], rows[i]):
            return False
    for i in range(len(cols)):
        if opt_dist([drawing[x][i] for x in range(len(rows))], cols[i]):
            return False
    return True
    

def solve_nonogram(x, y, rows, cols, reset_every = 2000, max_tries=10):
    drawing = reset_drawing(x, y)

    for i in range(1, reset_every*max_tries+1):
        best_fix = 0
        best_fix_index = []        
        wrong_cols = []
        wrong_rows = []

        for j in range(x):
            if opt_dist(drawing[j], rows[j]):
                wrong_rows.append(j)
        for j in range(y):
            if opt_dist([drawing[x][j] for x in range(x)], cols[j]):
                wrong_cols.append(j)
        
        if not wrong_cols and not wrong_rows:
            return drawing
        what_change = random.randint(0 if wrong_cols else 1, 1 if wrong_rows else 0)

        if what_change:
            row = random.choice(wrong_rows)
            for col in range(y):
                fix = opt_dist(drawing[row], rows[row]) + opt_dist([drawing[x][col] for x in range(x)], cols[col]) - after_switch(drawing, row, col, rows, cols)
                if fix > best_fix:
                    best_fix = fix
                    best_fix_index = [col]
                elif fix == best_fix:
                    best_fix_index.append(col)
            if best_fix_index:
                switch_pixel(drawing, row, random.choice(best_fix_index))
        else:
            col = random.choice(wrong_cols)
            for row in range(x):
                fix = opt_dist(drawing[row], rows[row]) + opt_dist([drawing[x][col] for x in range(x)], cols[col]) - after_switch(drawing, row, col, rows, cols)
                if fix > best_fix:
                    best_fix = fix
                    best_fix_index = [row]
                elif fix == best_fix:
                    best_fix_index.append(row)
            if best_fix_index:
                switch_pixel(drawing, random.choice(best_fix_index), col)

        if check_correctness(rows, cols, drawing):
            return drawing
        
        if i % reset_every == 0:
            drawing = reset_drawing(x, y)

    return drawing

def draw_nonogram(drawing):
    for row in drawing:
        print("".join(map(lambda x: "#" if x==1 else ".", row)))

def binary_to_hash(drawing):
    new_draw = []
    for row in drawing:
        new_draw.append("".join(map(lambda x: "#" if x else ".", row)))
    return new_draw

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

    answer = solve_nonogram(x, y, rows, cols)
    draw_nonogram(answer)
    answer = binary_to_hash(answer)

    with open(o, 'w') as o:
        for row in answer:
            o.write("".join(map(str, row)) + '\n')

if __name__ == '__main__':
    run()
    # pass