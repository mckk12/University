import json

# Getting the automaton from the chosen file
def load_automat(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Getting state change from dictionary
def get_state(current_state, letter, trans):
    return trans.get((current_state, letter), None)

# Getting the file path from the user
fp = input().strip()
with open(fp, "r") as l:
    lines=l
    
# Getting the automaton from the chosen file
f = lines.readline().strip()
automaton = load_automat(f)

# Creating a dictionary of transitions
trans={}
for transition in automaton['transitions']:
    trans[(transition["from"], transition["letter"])] = transition["to"]

# Running the automaton
current_state = automaton['initial']
while True:
            letter = lines.read(1)
            if letter == '\n':
                if current_state in automaton['accepting']:
                    print("yes")
                else:
                    print("no")
                current_state = automaton['initial']
            elif letter not in automaton["alphabet"]:
                break
            else:
                current_state = get_state(current_state, letter, trans)
                if current_state == None:
                    break
    
            