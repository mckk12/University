from itertools import product
import time

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

# Brute force solution
def brute(states_max, words_in, words_out):
    
    automat = {
        "alphabet": ["a", "b", "c"],
        "states": [],
        "initial": "",
        "accepting": [],
        "transitions": []
    }

    states = ["q" + str(i) for i in range(states_max)]

    # Generate all possible transitions
    trans_a = {i : [] for i in states}
    trans_b = {i : [] for i in states}
    trans_c = {i : [] for i in states}
    for i in states:
        trans_a[i] = product(["a"], [i], states)
        trans_b[i] = product(["b"], [i], states)
        trans_c[i] = product(["c"], [i], states)

    # Generate all possible automatons
    automatons = product(*[trans_a[i] for i in states], *[trans_b[i] for i in states], *[trans_c[i] for i in states])

    possible_automaton = None
    # options = []
    # Check each automaton
    for automaton in automatons:
        acc_states = {state: False for state in states}
        transitions_dict = {(t[0], t[1]): t[2] for t in automaton}
        flag = False

        for word in words_in:
            current_state = "q0"
            for letter in word:
                current_state = transitions_dict[(letter, current_state)]
            acc_states[current_state] = True

        for word in words_out:
            current_state = "q0"
            for letter in word:
                current_state = transitions_dict[(letter, current_state)]
            if acc_states[current_state]:
                flag = True
                break

        if not flag:
            # options.append(automaton)
            possible_automaton = (automaton, acc_states)
            break

    # print(options)
    if possible_automaton is None:
        return("Does not exist")
    else:
        # Creating automaton
        automat["states"] = states
        automat["initial"] = states[0]
        automat["transitions"] = [{"letter": t[0], "from": t[1], "to": t[2]} for t in possible_automaton[0]]
        automat["accepting"] = [state for state, acc in possible_automaton[1].items() if acc]
        return(automat)

def makeAutomaton(words_in, words_out):

    states = ["q0"]
    transitions = {}
    accepting = []
    start_state = "q0"
    i = 1

    for word in words_in:
        current_state = start_state

        for letter in word:
            if current_state not in transitions:
                transitions[current_state] = {}
            if letter not in transitions[current_state]:
                transitions[current_state][letter] = "q" + str(i)
                i+=1
                states.append(transitions[current_state][letter])
            current_state = transitions[current_state][letter]
        accepting.append(current_state)

    for word in words_out:
        current_state = start_state

        for letter in word:
            if current_state not in transitions:
                transitions[current_state] = {}
            if letter not in transitions[current_state]:
                transitions[current_state][letter] = "q" + str(i)
                i+=1
                states.append(transitions[current_state][letter])
            current_state = transitions[current_state][letter]

    automat = {
        "alphabet" : ["a", "b", "c"],
        "states" : states,
        "initial" : start_state,
        "accepting" : accepting,
        "transitions" : transitions
    }

    return automat

def addFillingState(transitions, states):
    new_state = "q" + str(len(states))
    states.append(new_state)
    for state in states:
        for letter in "abc":
            if state not in transitions:
                transitions[state] = {}
            if letter not in transitions[state]:
                transitions[state][letter] = new_state
    return transitions, states

def miniAutomaton(automaton):
    automaton["transitions"], automaton["states"] = addFillingState(automaton["transitions"], automaton["states"])
    transitions = automaton["transitions"]
    
    acc_states = automaton["accepting"]
    non_acc_states = [state for state in automaton["states"] if state not in acc_states]
   
    partitions = [acc_states, non_acc_states]

    start = time.time()
    while True:
        new_partitions = []
        for partition in partitions:
            pairs = product(partition, partition)
            possible_states = []
            for pair in pairs:
                if all(transitions[pair[1]][letter] == transitions[pair[0]][letter] for letter in "abc"):
                    if pair[0] in possible_states:
                        possible_states.remove(pair[0])
                    if pair[1] in possible_states:
                        possible_states.remove(pair[1])
                elif all(any(transitions[pair[1]][letter] in p and transitions[pair[0]][letter] in p for p in partitions) for letter in "abc"):
                    if pair[0] in possible_states:
                        possible_states.remove(pair[0])
                    if pair[1] in possible_states:
                        possible_states.remove(pair[1])
                else:
                    if pair[0] not in possible_states:
                        possible_states.append(pair[0])
                    if pair[1] not in possible_states:
                        possible_states.append(pair[1])
            part = []
            for state in partition:
                if state not in possible_states:
                    part.append(state)
            if possible_states != []:
                if len(part) > 0:
                    new_partitions.append(part)
                new_partitions.append(possible_states)
            else:
                new_partitions.append(partition)

            end = time.time() - start
            if end > 50:
                break
               
               
        if len(new_partitions) == len(partitions):
                break
        partitions = new_partitions

    new_transitions = {}
    for partition in partitions:
        for i in transitions:
            for letter in "abc":
                if transitions[i][letter] in partition:
                    transitions[i][letter] = partition[0]

    for partition in partitions:
        if partition[0] not in new_transitions:
                    new_transitions[partition[0]] = {}
        for state in partition:
            for letter in "abc":
                if letter not in new_transitions[partition[0]] and letter in transitions[state]:
                    new_transitions[partition[0]][letter] = transitions[state][letter]
    # print(len(partitions))

    transitions = []
    for transition in new_transitions:
        for letter in new_transitions[transition]:
            transitions.append({"letter" : letter,
                                "from" : transition,
                                "to" : new_transitions[transition][letter]})
            
    new_automaton = {
        "alphabet" : automaton["alphabet"],
        "states" : list(new_transitions.keys()),
        "initial" : automaton["initial"],
        "accepting" : list(set(i for i in automaton["accepting"] if i in new_transitions.keys())),
        "transitions" : transitions
    }
    
    return new_automaton

# Data for creating automaton
states_max, words_in, words_out = read_input()
words_in.sort(key=len)
words_out.sort(key=len)

if states_max < 4:
    automaton = brute(states_max, words_in, words_out)
else:
    automaton = makeAutomaton(words_in, words_out)
    automaton = miniAutomaton(automaton)

print(automaton)