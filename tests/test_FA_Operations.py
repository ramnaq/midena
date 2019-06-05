from model.FileUtil import import_FA
from model.FiniteAutomata import union


def tFA_Operations():
    tFA_Renaming_States()
    tFA_Union()


def tFA_Renaming_States():
    fa = import_FA('saves/myfirst.json')
    print('Original FA')
    print(fa)
    fa.rename_states(50)
    print('Renamed FA')
    print(fa)


def tFA_Union():
    fa = import_FA('saves/nfa_ends_with_zero.json')
    print('Original FA 1')
    print(fa)
    fb = import_FA("saves/test_FA_equalFirstLast.ext")
    print('Original FA 2')
    print(fb)

    fc = union(fa, fb)
    print('Union result')
    print(fc)

def test_FA_Operations():
    tFA_Operations()
    tFA_Renaming_States()
    tFA_Union()
