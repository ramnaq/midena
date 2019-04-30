import json

class FiniteAutomata():

    def __init__(self, sigma=[''], table={}, initial="", accepting=[""]):
        self.sigma = sigma
        self.table = table
        self.initial = initial
        self.accepting = accepting


    def states(self):
        return self.table.keys()
    

    def export_to(self, path):
        fa_json = {}
        fa_json["name"] = self.name
        fa_json["sigma"] = self.sigma
        fa_json["table"] = self.table
        fa_json["initial"] = self.initial
        fa_json["accepting"] = self.accepting

        fa_json["rg_str"] = self.grammar_str
        fa_json["regex_str"] = self.regex_str

        with open(path, 'w') as outfile:
            json.dump(fa_json, outfile)


    def __str__(self):
        t = self.table
        fastr = "";
        for state in t:
            fastr += state + ":\n"
            for symbol, transitions in t[state].items():
                fastr += "  "
                fastr += symbol + ": " + str(transitions) + "\n"
        return fastr


    """
        Load FA from JSON file
    """
    @staticmethod
    def import_from(path):
        data = json.load(open(path, 'r'))
        initial = data["initial"]
        accepting = data["accepting"]
        file_table = data["table"]
        sigma = []
        table = {}

        for state in file_table:
            if state not in table: table[state] = {}
            for symbol, transitions in file_table[state].items():
                if symbol not in sigma:
                    sigma.append(symbol) 
                if symbol not in table[state]:
                    table[state][symbol] = []
                for i in transitions:
                    table[state][symbol].append(i)
        fa = FiniteAutomata(sigma, table, initial, accepting)
        fa.name = data["name"]
        fa.regex_str = data["regex_str"]
        fa.grammar_str = data["rg_str"]
        return fa

