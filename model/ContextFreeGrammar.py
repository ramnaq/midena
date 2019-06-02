from model.FormalGrammar import FormalGrammar
from model.GrammarTypeValidator import CFGValidator


class ContextFreeGrammar(FormalGrammar):

    def __init__(self, symbols, sigma, prods, s, name="Context_Free_Grammar"):
        super().__init__(symbols, sigma, prods, s, name, CFGValidator())
        self.type = 2
