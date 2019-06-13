from model.FormalGrammar import FormalGrammar
from model.GrammarTypeValidator import CFGValidator


class ContextFreeGrammar(FormalGrammar):

    def __init__(self, symbols, sigma, prods, s, name="Context_Free_Grammar"):
        super().__init__(symbols, sigma, prods, s, name, CFGValidator())
        self.type = 2

    def chomskyNormalForm(self):
        # Eliminate the start symbol from right-hand sides
        self.productions.append(('T', [self.root]))

        # Eliminate rules with nonsolitary terminals
        p, b = 0, 0
        for prod in self.productions:
            for betas in prod[1]:
                replaceNonsolitaryTerminals(p, b)
                b += 1
            p += 1

    def eliminateEmptyProductions(self):
        ...

    def eliminateUnitRules(self):
        ...

    def eliminateUselessSymbols(self):
        ...

    def replaceNonsolitaryTerminals(self, p, b):
        i = 0
        for beta in betas:
            if (beta in sigma) and (beta > 1):
                # beta is a terminal symbol and it's not solitary, then
                # add a new nonterminal symbol ~beta, replace beta for it
                # and the rule (~beta -> beta)
                newNonterminal = '~' + beta
                self.symbols.append(newNonterminal)
                self.productions[p][b][i] = newNonterminal
                self.productions.append((newNonterminal, [beta]))
            i += 1

