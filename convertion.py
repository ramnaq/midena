import os
from model.FileUtil import importGrammar, export_FA
from model.regular_obj_conversion import regular_grammar_to_automata
from model.regular_obj_conversion import *

rg = importGrammar("/home/sidharta/workspace/midena/conv.ext")
fa = regular_grammar_to_automata(rg)
export_FA(fa, "/home/sidharta/workspace/midena/fa.ext")

