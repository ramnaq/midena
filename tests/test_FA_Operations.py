import utils

from model.FileUtil import import_FA
from model.FiniteAutomata import union, intersection


msgFAOperations = "TESTING FA OPERATIONS"

IN_FNAME = "saves/test_FA_myfirst.ext"
IN_FNAME1 = "saves/test_Nfa_ends_with_zero.ext"
IN_FNAME2 = "saves/test_FA_equalFirstLast.ext"
IN_FNAME3 = "saves/test_Intersection1.ext"
IN_FNAME4 = "saves/test_Intersection2.ext"


def tFA_Operations(fname=IN_FNAME, fname1=IN_FNAME1, fname2=IN_FNAME2, fname3=IN_FNAME3, fname4=IN_FNAME4):
    print("\nRENAME STATES")
    tFA_Renaming_States(fname)
    print("\nUNION")
    tFA_Union(fname1, fname2)
    print("\nCOMPLETE AUTOMATA")
    tFA_Complete(fname)
    print("\nINTERSECTION")
    tFA_Intersection(fname3, fname4)
    print("")


def tFA_Renaming_States(fname=IN_FNAME):
    fa = import_FA(fname)
    print(f'Original FA: {fa.name}')
    print(fa)
    rfa = fa.rename_states(100)
    print('Renamed FA')
    print(rfa)


def tFA_Union(fname1=IN_FNAME1, fname2=IN_FNAME2):
    fa = import_FA(fname1)
    print(f'Original FA 1: {fa.name}')
    print(fa)
    fb = import_FA(fname2)
    print(f'Original FA 2: {fb.name}')
    print(fb)

    fc = union(fa, fb)
    print('Union result')
    print(fc)


def tFA_Intersection(fname3=IN_FNAME3, fname4=IN_FNAME4):
    fa = import_FA(fname3)
    print(f'Original FA 1: {fa.name}')
    print(fa)
    fb = import_FA(fname4)
    print(f'Original FA 2: {fb.name}')
    print(fb)

    fc = intersection(fa, fb)
    print('Intersection result')
    print(fc)


def tFA_Complete(fname1=IN_FNAME1):
    fa = import_FA(fname1)
    print('Original FA 1')
    print(fa)

    print('Complete result')
    print(fa.complete())


def test_FA_Operations():
    infile = utils.promptFile(
        "FA to be renamed (e.g %s) [OPTIONAL]: " % IN_FNAME,
        optional=True)
    if infile == "":
        infile = IN_FNAME

    infile1 = utils.promptFile(
        "FA1 to do union (e.g %s) [OPTIONAL]: " % IN_FNAME1,
        optional=True)
    if infile1 == "":
        infile1 = IN_FNAME1

    infile2 = utils.promptFile(
        "FA2 to do union (e.g %s) [OPTIONAL]: " % IN_FNAME2,
        optional=True)
    if infile2 == "":
        infile2 = IN_FNAME2

    infile3 = utils.promptFile(
        "FA1 to do intersection (e.g %s) [OPTIONAL]: " % IN_FNAME3,
        optional=True)
    if infile3 == "":
        infile3 = IN_FNAME3

    infile4 = utils.promptFile(
        "FA2 to do intersection (e.g %s) [OPTIONAL]: " % IN_FNAME4,
        optional=True)
    if infile4 == "":
        infile4 = IN_FNAME4

    utils.startTestMsg(msgFAOperations)
    tFA_Operations(infile, infile1, infile2, infile3, infile4)
