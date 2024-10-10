import json
import sys

# Getting the automaton from the chosen file
def load_automat(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Getting state change (should add dict)
def get_state(automaton, current_state, letter):
    for option in automaton['transitions']:
        if option["from"] == current_state and option["letter"] == letter:
            return option["to"]

fp = input().strip()
automaton = load_automat(fp)

current_state = automaton['initial']
while True:
            letter = sys.stdin.read(1)
            if letter == '\n':
                if current_state in automaton['accepting']:
                    print("yes")
                else:
                    print("no")
                current_state = automaton['initial']
            elif letter not in automaton["alphabet"]:
                break
            else:
                current_state = get_state(automaton, current_state, letter)
        
            