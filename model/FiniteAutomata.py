import json
import copy

from model.RegularGrammar import RegularGrammar

class FiniteAutomata:

    def __init__(self, sigma=[''], table={}, initial="", accepting=[""]):
        self.sigma = sigma
        self.table = table
        self.initial = initial
        self.accepting = accepting
        self.name = 'newAutomata'
        self.grammar_str = ''
        self.regex_str = ''

    def states(self):
        return self.table.keys()

    def __str__(self):
        t = self.table
        fastr = ""
        for state in t:
            fastr += ('>' if state == self.initial else '') + \
                ('*' if state in self.accepting else '') + \
                state + ":\n"
            for symbol, transitions in t[state].items():
                fastr += "  "
                fastr += symbol + ": " + str(transitions) + "\n"
        return fastr

    def is_dfa(self):
        for state, transitions in self.table.items():
            if state is not self.initial and "&" in transitions:
                return False
            for tr in transitions.values():
                if len(tr) > 1:
                    return False
        return True

    def transition_to_text(self, transition):
        return "{" + ", ".join(sorted(transition)) + "}"

    def text_to_transition(self, text: str):
        try:
            text = text[1:-1]
            transition = text.split(',')
            transition = [x.strip() for x in transition]
            return transition
        except Exception as exc:
            print(f'Exception: {exc}')

    def update_sigma(self, prev, current):
        if prev == '':
            if current in self.sigma:
                print('Error: symbol already exists.')
                return
            self.sigma.append(current)
            for q in self.states():
                self.table[q][current] = '-'
            return
        self.sigma.remove(prev)
        self.sigma.append(current)
        self.sigma.sort()
        json_table = json.dumps(self.table)
        json_table = json_table.replace(prev, current)
        self.table = json.loads(json_table)

    def update_state(self, prev, st):
        if prev == '':
            self.add_state(st)
            return
        obj = {
            'sigma': self.sigma,
            'initial': self.initial,
            'accepting': self.accepting,
            'table': self.table
        }
        json_fa = json.dumps(obj)
        json_fa = json_fa.replace(prev, st)
        obj = json.loads(json_fa)
        self.sigma = obj['sigma']
        self.initial = obj['initial']
        self.accepting = obj['accepting']
        self.table = obj['table']

    def add_state(self, st):
        if st in self.states():
            print('Error: state already exists.')
            return
        self.table[st] = {x: '-' for x in self.sigma}

    def determinize(self):
        if self.is_dfa():
            return self

        dfa = FiniteAutomata(sigma=[x for x in self.sigma if x != '&'])
        dfa.accepting = []
        dfa.table = {}
        dfa.name = "Deterministic " + self.name

        initial = self.e_closure(self.initial)
        dfa.initial = self.state_from_list(initial)

        states_set = [initial]
        while len(states_set) > 0:
            states_tuple = states_set.pop()
            if type(states_tuple) == list:
                unified_state = self.state_from_list(states_tuple)
            else:
                unified_state = states_tuple
            if unified_state in dfa.states():
                continue
            dfa.table[unified_state] = {x: '-' for x in dfa.sigma}

            # check if is accepting state
            for accepting in self.accepting:
                if accepting in unified_state:
                    dfa.accepting += [unified_state]
                    break

            for symbol in dfa.sigma:
                transitions = []
                if type(states_tuple) == str:
                    states_tuple = [states_tuple]
                for q in states_tuple:
                    tr = self.e_closure_list(self.table[q][symbol])
                    transitions += [x for x in tr if x not in transitions]
                if transitions:
                    new_state = self.state_from_list(transitions)
                    states_set += [transitions] if transitions not in states_set else []
                    dfa.table[unified_state][symbol] = [new_state]
        return dfa

    def state_from_list(self, states_list):
        return ''.join(sorted(states_list))

    def e_closure(self, state: str) -> list:
        closure = set([state])
        if '&' not in self.table[state]:
            return list(closure)
        for st in self.table[state]['&']:
            if st == '-':
                return [state]
            closure.update(self.e_closure(st))
            return list(closure)

    def e_closure_list(self, states: list) -> list:
        closure = []
        for st in states:
            if st == '-':
                continue
            closure += self.e_closure(st)
        return closure

    def accept(self, sentence: str):
        det = self
        if not det.is_dfa():
            det = det.determinize()

        current_state = det.initial
        for c in sentence:
            if c not in det.sigma:
                return False
            current_state = det.table[current_state][c]
            if type(current_state) == list:
                current_state = current_state[0]
        return current_state in det.accepting
