#implement the algorithm to get from NFA to DFA
from read_from_file import read_from_file

nfa = read_from_file("inputs/nfae1.txt")
#nfa.print_self()

def epsilon_clausura(estado: set, transiciones):
    clausura = set()
    for simbolo in estado:
        clausura.add(simbolo)
    for transicion in transiciones:
        for simbolo in transicion[0]:
          if (simbolo in estado or simbolo in clausura) and transicion[1] == "EPSILON":
            for simbolo in transicion[2]:
                clausura.add(simbolo)
    return clausura


def get_states(estado: set, tranciones, letra):
    estados = set()
    for transicion in tranciones:
        ##(transicion, estado)
        for simbolo1 in transicion[0]:
            if (simbolo1 in estado or simbolo1 in estados) and transicion[1] == letra:
                for simbolo in transicion[2]:
                  estados.add(simbolo)
            
    return estados


def step(estado: set, transiciones, letra):
    clausura = epsilon_clausura(estado, transiciones)
    #print(clausura)
    estados = get_states(clausura, transiciones, letra)
    #print(estados)
    clausura2 = epsilon_clausura(estados, transiciones)
    #print(clausura2)
    return clausura2

#print(epsilon_clausura({"A"}, nfa.transitions))
##print(get_states({"A"}, nfa.transitions, "0"))



for state in nfa.states:
    for letter in nfa.alphabet:
        print(step(state, nfa.transitions, letter))
        print("----")