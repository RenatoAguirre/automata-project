from automata import Automata


def read_from_file(file_path: str) -> Automata:
    with open(file_path, "r") as file:
        start_state = str()
        end_states = list()
        states = list()
        alphabet = list()
        file.readline() #ignore the first line, we now it's always "estado"
        start_state = file.readline().strip()[1] #the next one its always the starting state
        states.append(start_state)
        for line in file:
            line = line.strip().upper()
            if line == "ALFABETO":
                break
            elif line.startswith("*"):
                end_states.append(line[1:])
                states.append(line[1:])
            else:
                states.append(line)
            
        for line in file:
            line = line.strip().upper()
            if line == "TRANSICIONES":
                break
            else:
                alphabet.append(line.strip())

        #transitions
        transitions = list()
        for line in file:
            line = line.strip().upper()
            if "EPSILON" in line:
                transitions.append((line[0], "EPSILON", line[-1]))
            else:
                transitions.append((line[0], line[2], line[-1]))

    return Automata(states, alphabet, transitions, start_state, end_states)
            

if __name__ == "__main__":
    automata = read_from_file("inputs/dfa_input.txt")
    automata.print_self()