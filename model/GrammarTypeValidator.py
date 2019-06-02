from abc import ABC, abstractmethod


'''
GrammarTypeValidator is the abstract class of the Strategy patterns. It defines
an interface for validating grammars of specific types.

The specializations of this class are responsible for verifying if a given
grammar really is of a specific type.
'''
class GrammarTypeValidator(ABC):

    @abstractmethod
    def validProductions(self, grammar):
        '''Say that 2 is the grammar type that the class which implements this
            method is commited to deal with. Then:
            Return
                True if the given grammar follows all the rules for grammars of
                    type 2.
                False otherwise.
        '''
        ...

    def nonTerminalAlphas(self, grammar):
        '''Return
                True if each "alpha" of the grammar's productions is a single
                    non-terminal symbol.
                False otherwise.
        '''
        for p in grammar.productions:
            if (p[0] not in grammar.symbols) or (p[0] in grammar.sigma):
                return False
        return True



class RGValidator(GrammarTypeValidator):
    def validProductions(self, grammar):
        '''Return
            True if the given grammar follows all the rules for grammars of
                type 3.
            False otherwise.

            Note: this method modifies the attribute 'productions' of the given
                grammar. The updating alters the form of the 'productions',
                because it considers that strings longer that 1 can represent
                a single non-Terminal symbol, for example: Q_1. That way, a
                production 'N -> aQ_1' will have the form (N, [a, Q_1]).
        '''
        symbols, sigma = grammar.symbols, grammar.sigma
        regularProductions = []
        i = 0

        if not super().nonTerminalAlphas(grammar):
            return False

        for p in grammar.productions:
            regularProductions.append([p[0], []])
            for beta in p[1]:

                # The first symbol of the substitution must be terminal
                if (beta[0] not in sigma):
                    return False
                if (len(beta) > 1):

                    # The second symbol of the substitution must be non-terminal
                    if (beta[1] in sigma) or (beta[1:] not in symbols):
                        return False
                    else:
                        beta = [beta[0], beta[1:]]  # (A -> aB_1) beta = [a, B_1]
                else:
                    beta = [beta[0]]
                regularProductions[i][1].append(beta)
            i += 1
        rgProductions = list(map(lambda p: tuple(p), regularProductions))
        grammar.updateProductions(rgProductions)

        return True


class CFGValidator(GrammarTypeValidator):
    def validProductions(self, grammar):
        '''Return
            True if the given grammar follows all the rules for grammars of
                type 2.
            False otherwise.

            Note: this method modifies the attribute 'productions' of the given
                grammar. A single production A -> aSa, for example, will have
                the form (A, [a, S, a]).
        '''
        if RGValidator().validProductions(grammar):
            # If grammar is a RG, then it is also a valid CFG
            return True

        symbols, sigma = grammar.symbols, grammar.sigma
        cfgProductions = []
        i = 0

        for p in grammar.productions:
            cfgProductions.append([p[0], []])
            for beta in p[1]:

                # All substitutions of production p must follow the rules of the
                # rules for grammars of type 2
                cfgSubstitutions =\
                    self.cfgSubstitutions(beta, symbols, sigma)
                if len(cfgSubstitutions) != len(beta):
                    return False
                else:
                    beta = cfgSubstitutions
                cfgProductions[i][1].append(beta)
            i += 1
        cfgProductions = list(map(lambda p: tuple(p), cfgProductions))
        grammar.updateProductions(cfgProductions)

        return True

    def cfgSubstitutions(self, substitutions, symbols, sigma):
        '''Returns the substitutions that attends the rule for CFG's:
            For a produciton α -> β, then β ∈ (N ∪ T)*, where N = symbols and
            T = sigma.
        '''
        return list(filter(
            lambda s: (s in symbols) or (s in sigma),
            substitutions))


class CSGValidator(GrammarTypeValidator):
    def validProductions(self, grammar):
        ...
