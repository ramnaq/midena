import os
from model.FileUtil import importGrammar, export_FA
from model.regular_obj_conversion import regular_grammar_to_automata
from model.regular_obj_conversion import *

print("Importing grammar...")
rg = importGrammar("/home/sidharta/workspace/midena/conv.ext")

print("Converting grammar to Finite Automata...")
fa = regular_grammar_to_automata(rg)

print("Exporting Automata in fa.ext")
export_FA(fa, "/home/sidharta/workspace/midena/fa.ext")

