class RegularGrammar():

    def __init__(self, symbols, sigma, prods, s, name="Regular_Grammar"):
        if not (symbols and sigma and prods and s):
            raise ValueError("Parameters must not be null.")
        #if not self.is_regular(symbols, sigma, prods, s):
        #    raise ValueError("Not Regular Grammar.")

        self.symbols = symbols
        self.sigma = sigma
        self.productions = prods
        self.define_root(s)
        self.name = name

    def is_regular(self, symbols, sigma, prods, s):
        for p in prods:
            if (p[0] not in symbols) or (p[0] in sigma):
                return False
            for beta in p[1]:
                if (len(beta) > 2) or (beta[0] not in sigma):
                    return False
                elif (len(beta) == 2) and\
                        ((beta[1] in sigma) or (beta[1] not in symbols)):
                    return False
        return True

    def define_root(self, s):
        if (self.symbols is not None) and (s not in self.symbols):
            self.root = s

    def add_production(self, p):
        self.productions.append(p)

    def derivate(self, iform, n):
        pass

    def apply_productions(self, w):
        pass


if __name__ == "__main__":
    # alphabet: {0,1} and starts with 0
    s = ("S", ["0A", "0"])
    a = ("A", ["0A", "1A", "0", "1"])
    productions = [s, a]
    rg = RegularGrammar(symbols="SA01", sigma="01", prods=productions, s='S')

    # not Regular Grammars
    print("N: non terminals, T: terminals, X: something")
    s = ("S", ["0A", "0"])
    a = ("A", ["0A", "10", "0", "1"])  # N -> TT
    b = ("A", ["0A", "1B", "0", "1"])  # N -> TX
    c = ("A", ["0A", "B1", "0", "1"])  # N -> XT
    d = ("A", ["0A", "AA", "0", "1"])  # N -> NN
    e = ("A", ["0A", "BA", "0", "1"])  # N -> XN
    prods1 = [s, a]
    prods2 = [s, b]
    prods3 = [s, c]
    prods4 = [s, d]
    prods5 = [s, e]

    try:
        rg = RegularGrammar(symbols="SA01", sigma="01", prods=prods1, s='S')
    except ValueError:
        print("[ERROR] Production N -> TT")

    try:
        rg = RegularGrammar(symbols="SA01", sigma="01", prods=prods2, s='S')
    except ValueError:
        print("[ERROR] Production N -> TX")

    try:
        rg = RegularGrammar(symbols="SA01", sigma="01", prods=prods3, s='S')
    except ValueError:
        print("[ERROR] Production N -> XT")

    try:
        rg = RegularGrammar(symbols="SA01", sigma="01", prods=prods4, s='S')
    except ValueError:
        print("[ERROR] Production N -> NN")

    try:
        rg = RegularGrammar(symbols="SA01", sigma="01", prods=prods5, s='S')
    except ValueError:
        print("[ERROR] Production N -> XN")
