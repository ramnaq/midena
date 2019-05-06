from model.FileUtil import import_FA

dfa = import_FA('saves/nfa.json')
print(dfa)
print(dfa.determinize())
