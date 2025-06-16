'''
For every possible window size D of ones we check how many bit changes it will need in the current sequence to achieve it and then we choose the fewest one.
For that we just need to iterate over the sequence and count zeros inside and ones outside of the current window. Then remember only the fewest changes.
'''

def opt_dist(seq, num):
    changes = len(seq) + 1
    for i in range(len(seq) - num + 1):
        curr = seq[i:i+num]
        rest = seq[:i] + seq[i+num:]
        changes = min(curr.count("0") + rest.count("1"), changes)
    return changes


# print(opt_dist("11111111111", 5))
# print(opt_dist("0010001000", 4))
# print(opt_dist("0010001000", 3))
# print(opt_dist("0010001000", 2))
# print(opt_dist("0010001000", 1))
# print(opt_dist("0010001000", 0))

input_file = open("zad4_input.txt", "r")
output_file = open("zad4_output.txt", "w")
results = []
for line in input_file.readlines():
    sequence, number = line.strip().split()
    results.append(str(opt_dist(sequence, int(number))))

output_file.write("\n".join(results))
input_file.close()
output_file.close()