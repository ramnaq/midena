import json


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
            fastr += state + ":\n"
            for symbol, transitions in t[state].items():
                fastr += "  "
                fastr += symbol + ": " + str(transitions) + "\n"
        return fastr

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
            if current in self.current_fa.sigma:
                print('Error: symbol already exists.')
                return
            self.current_fa.sigma.append[current]
            return
        self.sigma.remove(prev)
        self.sigma.append(current)
        self.sigma.sort()
        json_table = json.dumps(self.table)
        json_table = json_table.replace(prev, current)
        self.table = json.loads(json_table)

    def update_state(self, prev, st):
        if prev == '':
            if st in self.current_fa.states():
                print('Error: state already exists.')
                return
            self.table[st] = {x: '-' for x in self.sigma}
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
