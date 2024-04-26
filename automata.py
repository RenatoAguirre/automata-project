class Automata:
    # create an automata class
    def __init__(
        self,
        states: list[str],
        alphabet: list[str],
        transitions: list[tuple],
        end_state: str,
        accept_states,
    ):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = end_state
        self.end_states = accept_states

    def print_self(self):
        print(
            f"States: {self.states}, Alphabet: {self.alphabet}, Transitions: {self.transitions}, Start State: {self.start_state}, End States: {self.end_states}"
        )
