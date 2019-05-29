import json

from model.RegularGrammar import RegularGrammar
from model.Minimization import Partition, Group


class FiniteAutomata():

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

    def toRegularGrammar(self):
        name = self.name + "Grammar"
        root = self.initial
        sigma = set(self.sigma)

        faStates = self.states()
        grammarStates = list(map(lambda s: self._grammarSymbol(s), faStates))
        symbols = set(grammarStates)

        productions = []

        for state in faStates:
            stateTransictions = self.table[state]
            alpha = self._grammarSymbol(state)
            beta = []
            for symbol in self.sigma:
                if symbol in stateTransictions.keys():
                    nextStates =\
                        self._nextStatesSeparated(stateTransictions, symbol)
                    beta += list(map(
                        lambda ns: symbol + self._grammarSymbol(ns),
                        nextStates)
                    )
                    if state in self.accepting:
                        beta.append(symbol)
            productions.append((alpha, beta))

        return RegularGrammar(symbols, sigma, productions, root, name)

    def _grammarSymbol(self, state):
        return "_".join(state.upper())

    def _nextStatesSeparated(self, transitions, symbol):
        nextStates = []
        for ns in transitions[symbol]:
            nextStates += ns.split(", ")
        return nextStates

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

    def minimize(self):
        det = self
        if not det.is_dfa():
            det = det.determinize()

        final = set(det.accepting)
        non_final = set(det.states())
        non_final.difference_update(final)
        partK_1 = Partition({Group(final), Group(non_final)})
        partK = Partition()

        while partK != partK_1:
            partK_1 = partK
            partK = Partition()
            for group in partK_1:
                for elem in group:
                    g = det.fit_in_group(elem, partK)
                    if g:
                        g.add(elem)
                    else:
                        partK.add(Group([elem]))
        # Create new Automata
        minimized = FiniteAutomata(det.sigma)
        while len(partK.groups) > 0:
            states_group = partK.pop()  # {q1, q3}
            unified_state = self.state_from_list(states_group)  # q1q3
            minimized.table[unified_state] = {x: '-' for x in det.sigma}

            # check if it is accepting state
            for st in states_group:
                if st in det.accepting:
                    minimized.accepting.append(unified_state)
                    break

            for symbol in minimized.sigma:
                for e in states_group:  
                    break  # beautiful python
                *** e is the first element ***
                """
                pegar a transicao tr de e
                get_group G em que tá tr
                unif_state de G
                se nao ta em minimized.states:
                    add unif
                minimized[unified_state] =/add {symbol: unif}
                
                
                for q in states:
                    tr = self.e_closure_list(self.table[q][symbol])
                    transitions += [x for x in tr if x not in transitions]
                if transitions:
                    new_state = self.state_from_list(transitions)
                    states_set += [transitions] if transitions not in states_set else []
                    dfa.table[unified_state][symbol] = [new_state]
        return dfa



    def fit_in_group(self, elem, partition) -> Group:
        for group in partition.groups:
            if self.equivalence(elem, group[0], partition):
                return group
        return None

    def equivalence(self, a, b, partition) -> bool:
        for s in self.sigma:
            dest1 = self.table[a][s][0]
            dest2 = self.table[b][s][0]
            if dest1 not in partition.group_of(dest2):
                return False
        return True
