import os

from utils import regular_grammar_to_automata, finite_automata_to_grammar
from model.FileUtil import importGrammar, import_FA
from model.regular_obj_conversion import *

rgFileName = "saves/test_RG_equalFirstLast.ext"
faFileName = "saves/test_FA_equalFirstLast.ext"

def testRGtoFiniteAutomataConversion():
    rg = importGrammar(rgFileName)
    print("Grammar to be converted ({}):".format(rg.name))
    print(str(rg))

    print("Converting to Finite Automata...")
    fa = rg_to_fa(rg)
    print(str(fa))

def testFAtoRegularGrammarConversion():
    fa = import_FA(faFileName)
    print("Automata to be converted ({}):".format(fa.name))
    print(str(fa))

    print("Converting to Regular Grammar...")
    fa = fa_to_rg(fa)
    print(str(fa))

def test_RegularConversions():
    testRGtoFiniteAutomataConversion()
    testFAtoRegularGrammarConversion()
