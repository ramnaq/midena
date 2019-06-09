import utils

from model.FileUtil import import_FA
from model.FiniteAutomata import union


msgFAOperations = "TESTING FA OPERATIONS"

IN_FNAME = "saves/test_FA_myfirst.ext"
IN_FNAME1 = "saves/test_Nfa_ends_with_zero.ext"
IN_FNAME2 = "saves/test_FA_equalFirstLast.ext"


def tFA_Operations(fname=IN_FNAME, fname1=IN_FNAME1, fname2=IN_FNAME2):
    # tFA_Renaming_States(fname)
    tFA_Union(fname1, fname2)


def tFA_Renaming_States(fname=IN_FNAME):
    fa = import_FA(fname)
    print('Original FA')
    print(fa)
    fa.rename_states(50)
    print('Renamed FA')
    print(fa)


def tFA_Union(fname1=IN_FNAME1, fname2=IN_FNAME2):
    fa = import_FA(fname1)
    print('Original FA 1')
    print(fa)
    fb = import_FA(fname2)
    print('Original FA 2')
    print(fb)

    fc = union(fa, fb)
    print('Union result')
    print(fc)


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

    utils.startTestMsg(msgFAOperations)
    tFA_Operations(infile, infile1, infile2)
