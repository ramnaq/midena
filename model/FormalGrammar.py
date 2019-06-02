from abc import ABC, abstractmethod

from model.GrammarTypeValidator import RGValidator


class FormalGrammar(ABC):

    def __init__(self, symbols, sigma, prods, s, name="Grammar",
            grammarValidator=RGValidator):
        if not (symbols and sigma and prods and s):
            raise ValueError("Parameters must not be null.")

        self.symbols = symbols
        self.sigma = sigma
        self.productions = prods
        self.define_root(s)
        self.name = name

        if not grammarValidator.validProductions(self):
            raise ValueError("Invalid grammar type.")

    def updateProductions(self, prods):
        self.productions = prods

    def define_root(self, s):
        if (self.symbols is not None) and (s not in self.symbols):
            self.root = s

    def derivate(self, iform, n):
        pass

    def apply_productions(self, w):
        pass

