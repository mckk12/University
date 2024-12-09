# Based of the article https://www.cs.cmu.edu/~mheule/publications/bnaic2009.pdf


from itertools import product
from collections import defaultdict as dd

# Reading input
def read_input():
    n, m = map(int, input().split())

    words_in = []
    words_out = []
    for _ in range(n):
        word = input().strip()
        if word[0] == '-':
            words_out.append(word[1:])
        else:
            words_in.append(word[1:])
    return m, words_in, words_out  

class APTA:
    def __init__(self, positive_words, negative_words):
        self.root = None
        self.alphabet ="abc"
        self.states = []
        self.accepting_states = []
        self.rejecting_states = []
        self.positive_words = positive_words
        self.negative_words = negative_words
        self.transitions = dd(lambda: {i: None for i in "abc"})
        self.ineq_constr = []

    class __Node():
        def __init__(self, name):
            self.name = name
            self.parents = []
            self.transitions = {i: None for i in "abc"}
            self.is_accepting = None

    def create_apta(self):
        words_in = self.positive_words
        words_out = self.negative_words
        self.root = self.__Node(0)
        self.states = [self.root]
        for word in words_in:
            current_node = self.root
            for letter in word:
                if current_node.transitions[letter] is None:
                    new_node = self.__Node(len(self.states))
                    new_node.name = len(self.states)
                    current_node.transitions[letter] = new_node
                    self.transitions[current_node.name][letter] = new_node.name
                    new_node.parents.append((current_node, letter))
                    self.states.append(new_node)
                    current_node = new_node
                else:
                    current_node = current_node.transitions[letter]
            current_node.is_accepting = True
            if current_node not in self.accepting_states:
                self.accepting_states.append(current_node)

        for word in words_out:
            current_node = self.root
            for letter in word:
                if current_node.transitions[letter] is None:
                    new_node = self.__Node(len(self.states))
                    new_node.name = len(self.states)
                    current_node.transitions[letter] = new_node
                    self.transitions[current_node.name][letter] = new_node.name
                    new_node.parents.append((current_node, letter))
                    self.states.append(new_node)
                    current_node = new_node
                else:
                    current_node = current_node.transitions[letter]
            current_node.is_accepting = False
            if current_node not in self.rejecting_states:
                self.rejecting_states.append(current_node)

    def create_ineq_constr(self):
        for state in self.states:
            for state2 in self.states:
                if state == state2:
                    continue
                if state.is_accepting != state2.is_accepting and state.is_accepting is not None and state2.is_accepting is not None:
                    if (state2, state) not in self.ineq_constr:
                        self.ineq_constr.append((state, state2))
    
    def to_sat(self, max_states):
        # names of variables
        xs = [[i+j*max_states for i in range(1, max_states + 1)] for j in range(len(self.states))]
        ys = [[[i+(j*max_states+k)*max_states + xs[-1][-1] for i in range(1, max_states+1)] for k in range(max_states)]for j in range(len(self.alphabet))]
        zs = [i+ys[-1][-1][-1] for i in range(1, max_states + 1)]

        num_vars = max_states * len(self.states) + max_states * max_states * len(self.alphabet) + max_states
        # num_clauses = len(self.states) * max_states + 2 * max_states * len(self.accepting_states) * len(self.rejecting_states) + len(self.states) * max_states * max_states + len(self.alphabet) * max_states**3
        
        # print("p cnf", num_vars, num_clauses)
        claus_count = 0
        to_print = []
        for i in xs:
            # print(" ".join(map(str, i + [0])))
            to_print.append(i + [0])
            claus_count += 1

        for i in range(len(self.accepting_states)):
            for j in range(len(self.rejecting_states)):
                for k in range(max_states):
                    # print(-xs[self.accepting_states[i].name][k], zs[k], 0)
                    to_print.append((-xs[self.accepting_states[i].name][k], zs[k], 0))
                    # print(-xs[self.rejecting_states[j].name][k], -zs[k], 0)
                    to_print.append((-xs[self.rejecting_states[j].name][k], -zs[k], 0))
                    claus_count += 2
        
        alph_map = {"a": 0, "b": 1, "c": 2}
        for v in self.states:
            for i in range(max_states):
                for j in range(max_states):
                        if len(v.parents)>0:
                            # print(v.name, v.parents[0][0].transitions[v.parents[0][1]].name)
                            # print(ys[alph_map[v.parents[0][1]]][i][j], -xs[v.parents[0][0].name][i], xs[v.name][j], 0)
                            claus_count += 1
                            to_print.append((ys[alph_map[v.parents[0][1]]][i][j], -xs[v.parents[0][0].name][i], -xs[v.name][j], 0))

        for a in range(len(self.alphabet)):
            for h in range(max_states):
                for i in range(max_states):
                    for j in range(max_states):
                        if h < j:
                            # print(-ys[a][i][h], -ys[a][i][j], 0)
                            to_print.append((-ys[a][i][h], -ys[a][i][j], 0))
                            claus_count += 1

        print("p cnf", num_vars, claus_count)
        for i in to_print:
            print(" ".join(map(str,i)))
        # with open("file.txt", "w") as f:
        #     f.write(f"p cnf {num_vars} {claus_count}\n")
        #     for clause in to_print:
        #         f.write(" ".join(map(str, clause)) + "\n")


# Data for creating automaton
states_max, words_in, words_out = read_input()

apta = APTA(words_in, words_out)
apta.create_apta()
# apta.create_ineq_constr()
apta.to_sat(states_max)