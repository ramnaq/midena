from model.FormalGrammar import FormalGrammar
from model.GrammarTypeValidator import CFGValidator


class ContextFreeGrammar(FormalGrammar):

    def __init__(self, symbols, sigma, prods, s, name="Context_Free_Grammar"):
        super().__init__(symbols, sigma, prods, s, name, CFGValidator())
        self.type = 2

    def chomskyNormalForm(self):
        # 1. Elimination of the start symbol from right-hand sides
        self.productions.append(("S'", [self.root]))
        self.root = "S'"

        # 2. Removal of Null Productions
        self.removeNullProductions()

        # 3. Removal of Unit Productions
        self.removeUnitProductions()

        '''
        # Eliminate rules with nonsolitary terminals
        p, b = 0, 0
        for prod in self.productions:
            for betas in prod[1]:
                replaceNonsolitaryTerminals(p, b)
                b += 1
            p += 1
        '''

    def removeNullProductions(self):
        '''This method removes all null productions of self.productions.

        A production is null when it contains at least one nullable symbol.
        A non-terminal symbol A is nullable if there is a production A -> ε or
        if there is a derivation that starts at A and leads to ε (A -> ...  ->
        ε).
        '''
        nullableSet = self.nullableNonTerminals()

        # Replacement of nullable symbols for ε
        newProds = []
        for prod in self.productions:
            substitutions = []

            for beta in prod[1]:
                nullableInBeta = set(filter(lambda b: b in nullableSet, beta))
                if len(nullableInBeta) > 0:
                    substitutions +=\
                        self.nullablesRemoval(nullableInBeta, beta)
                    if len(beta) > 1 or\
                            (beta[0] not in nullableInBeta and b != 'ε'):
                        substitutions += prod[1]
                    self.removeReplicated(substitutions)

            if substitutions != []:
                newProds.append((prod[0], substitutions))
            else:
                betas = list(filter(
                    lambda beta: len(beta) > 1 or
                        (beta[0] not in nullableSet and beta[0] != 'ε'),
                    prod[1]))
                if len(betas) != 0:
                    newProds.append((prod[0], betas))

        self.productions = newProds

    def nullableNonTerminals(self):
        '''Returns a set with all nullable non-terminal symbols.'''
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

    def nullablesRemoval(self, nullableSet, beta):
        substitutions = []

        # Add new the resulting substitutions for each nullable symbol
        for n in nullableSet:
            substitutions += self.nullableRemoval(n, beta)

        return substitutions

    def nullableRemoval(self, nullable, beta):
        newSubstitutions = [beta]

        # Base recursion case
        if (len(beta) == 1):
            if beta[0] == nullable:
                newSubstitutions.pop(0)
            return newSubstitutions

        i = 0
        for s in beta:
            if s == nullable:
                btemp = beta.copy()
                btemp.pop(i)
                newSubstitutions += self.nullableRemoval(nullable, btemp)
            i += 1

        return newSubstitutions

    def removeReplicated(self, arr):
        # TODO move this function from here
        for s in arr:
            ocurrencies = arr.count(s)
            if ocurrencies > 1:
                for i in range(0, ocurrencies - 1):
                    arr.remove(s)
        return arr

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

