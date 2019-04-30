class FiniteAutomata():

    def __init__(self, sigma=[''], table={}, initial="", accepting=[""]):
        self.sigma = sigma
        self.table = table
        self.initial = initial
        self.accepting = accepting

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
