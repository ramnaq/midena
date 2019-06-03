from model.FileUtil import import_FA


def tFA_Determinization():
    fa = import_FA('saves/test_determinization.json')
    print('Original NFA')
    print(fa)
    m = fa.determinize()
    print('Determinized FA')
    print(m)
    fa = import_FA('saves/nfa_ends_with_zero.json')
    print('Second test\n')
    print('Other NFA')
    print(fa)
    m = fa.determinize()
    print('Determinized FA')
    print(m)
