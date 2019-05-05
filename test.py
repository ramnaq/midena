from model.FileUtil import import_FA

dfa = import_FA('tests/other_fa2.json')
print(dfa)
print(dfa.initial)
print(dfa.e_closure(dfa.initial))
print(dfa.determinize())
