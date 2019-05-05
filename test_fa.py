from model.FileUtil import import_FA

dfa = import_FA('tests/myfirst.json')
print(dfa)
print(dfa.determinize())
