
# Creating dictionary for automaton
automat = {
    "alphabet" : [],
    "states" : [],
    "initial" : "",
    "accepting" : [],
    "transitions" : [{ "letter" : "", "from" : "", "to" : "" }]
}


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

# Data for creating automaton
states_max, words_in, words_out = read_input()

# Creating automaton
trans_helper = [{ "letter" : "", "from" : "", "to" : "" }]
for i in range(states_max):
    automat["states"].append('q' + str(i + 1))
automat["initial"] = automat["states"][0]
automat["alphabet"] = list(set(i for i in (''.join(words_in + words_out))))
for state in automat["states"]:
    for letter in automat["alphabet"]:
        automat["transitions"].append({ "letter" : letter, "from" : state, "to" : ''})

# te same litery pod rzad == max stanów -> litera zapetla sie w jednym stanie // zapetlenie 2 stanow??

        