from model.FormalGrammar import FormalGrammar
from model.GrammarTypeValidator import CFGValidator


class ContextFreeGrammar(FormalGrammar):

    def __init__(self, symbols, sigma, prods, s, name="Context_Free_Grammar"):
        super().__init__(symbols, sigma, prods, s, name, CFGValidator())
        self.type = 2

    def chomskyNormalForm(self):
        # 1. Elimination of the start symbol from right-hand sides
        self.productions.append(("S'", [[self.root]]))
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
        '''Removes all null productions of self.productions.

        A production is null when it contains at least one nullable symbol.
        A non-terminal symbol A is nullable if there is a production A -> ε or
        if there is a derivation that starts at A and leads to ε (A -> ...  ->
        ε).
        '''
        nullableSet = self.nullableNonTerminals()

        # Replacement of nullable symbols for ε (removal of nullable symbols)
        while len(nullableSet) != 0:
            for prod in self.productions:
                substitutions = []

                for beta in prod[1]:
                    nullableInBeta = set(filter(lambda b: b in nullableSet, beta))
                    while len(nullableInBeta) != 0:
                        nb = nullableInBeta.pop()
                        self.nullableRemoval(nb)
                        nullableSet.discard(nb)
                        nullableInBeta.discard(nb)

    def removeUnitProductions(self):
        prodsDict = self.productionsDictionary()
        newProds = self.productions.copy()

        while self.countUnitProductions() != 0:
            for prod in self.productions:
                for beta in prod[1]:
                    if len(beta) == 1 and beta[0] in self.symbols:
                        self.removeUnitProduction(newProds, prod, beta[0])
            self.productions = newProds

    def removeUnitProduction(self, newProds, prod, symbol):
        currProdBeta = prod[1].copy()
        currProdBeta.remove([symbol])
        symbolProdBeta = self.productionsDictionary()[symbol]

        newProds.remove(prod)
        newProds.append((prod[0], currProdBeta + symbolProdBeta))

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

    def nullableRemoval(self, nullable):
        '''Removes 'nullable' non terminal symbol from all productions'''
        newProductions = self.productions.copy()

        for prod in self.productions:
            substitutions = []

            for beta in prod[1]:
                nullableInBeta = set(filter(lambda b: nullable in b, beta))
                if len(nullableInBeta) == 1:
                    # 'nullable' is present in some substitution
                    substitutions += self.removeNullable(nullable, beta)
                    self.removeReplicated(substitutions)

            self.newProductionsUpdating(
                    newProductions, prod, substitutions, nullable)

        self.productions = newProductions

    def removeNullable(self, nullable, beta):
        '''Recursively replaces all 'nullable' symbols from the given beta
        with 'ε', that is, to remove them, in all possible combinations.
        returning a list of the resulting beta's.

        Return a list of the new beta's.
        '''
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
                newSubstitutions += self.removeNullable(nullable, btemp)
            i += 1

        return newSubstitutions

    def countUnitProductions(self):
        counter = 0
        for prod in self.productions:
            for beta in prod[1]:
                if len(beta) == 1 and beta[0] in self.symbols:
                    counter += 1
        return counter

    def removeReplicated(self, arr):
        '''Removes all replicated elements of the given list'''
        # TODO move this function from here
        for s in arr:
            ocurrencies = arr.count(s)
            if ocurrencies > 1:
                for i in range(0, ocurrencies - 1):
                    arr.remove(s)

    def newProductionsUpdating(
            self, newProductions, prod, substitutions, nullable):
        '''Add to newProductions a new production, accordingly the given
        nullable symbol. If the head of prod is nullable, then the new
        production must not produce ε.

        If substitutions is empty, the original substitutions from prod
        will be used. Otherwise, substitutions itself.

        newProductions is a specific state of self.productions being
        updated on removal of null productions.
        '''
        newProd = None

        def removeEmptySymbol(substitutions):
            return list(filter(lambda s: 'ε' not in s, substitutions))

        if substitutions != []:
            if prod[0] == nullable:
                substitutions = removeEmptySymbol(substitutions)
            newProd = (prod[0], substitutions)
        else:
            betas = prod[1]
            if prod[0] == nullable:
                betas = removeEmptySymbol(betas)
            if len(betas) != 0:
                newProd = (prod[0], betas)

        if newProd is not None:
            newProductions.remove(prod)
            newProductions.append(newProd)

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

