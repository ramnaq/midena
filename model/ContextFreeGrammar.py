from model.FormalGrammar import FormalGrammar
from model.GrammarTypeValidator import CFGValidator


class ContextFreeGrammar(FormalGrammar):

    def __init__(self, symbols, sigma, prods, s, name="Context_Free_Grammar"):
        super().__init__(symbols, sigma, prods, s, name, CFGValidator())
        self.type = 2

    def chomskyNormalForm(self):
        self.removeNullProductions()
        '''
        # Eliminate the start symbol from right-hand sides
        self.productions.append(('T', [self.root]))
        self.root = 'T'

        self.removeNullProductions()
        # Eliminate rules with nonsolitary terminals
        p, b = 0, 0
        for prod in self.productions:
            for betas in prod[1]:
                replaceNonsolitaryTerminals(p, b)
                b += 1
            p += 1
        '''

    def removeNullProductions(self):
        nullable = self.nullableNonTerminals()
        print(nullable)
        # more soon

    def nullableNonTerminals(self):
        '''Returns a set with all non-terminal symbols. A is nullable if there
            is a production A -> ε or if there is a derivation that starts at
            A and leads to ε (A -> ... -> ε)
        '''
        nullableSet = set()

        def isDirectNullable(symbol):
            return symbol == 'ε'

        def isIndirectNullable(symbol):
            return symbol in nullableSet

        def nullable(func):
            for prod in self.productions:
                isNull = False

                for beta in prod[1]:
                    if (len(beta) == 1) and func(beta[0]):
                        # the non-terminal prod[0] is replaced by at least one
                        # empty symbol, then it is a nullable non-terminal
                        isNull = True
                        break

                if isNull:
                    nullableSet.add(prod[0])

        # adds to nullableSet all direct nullable symbols
        nullable(isDirectNullable)
 
        # adds to nullableSet all remaining (indirect) nullable symbols
        nullable(isIndirectNullable)

        return nullableSet

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

