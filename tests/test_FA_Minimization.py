import utils

from model.FileUtil import import_FA


msgFAMinimization = "TESTING FA MINIMIZATION"
IN_FNAME = "saves/test_Minimization.ext"


def tFA_Minimization(fname=IN_FNAME):
    fa = import_FA(fname)
    print('Original FA')
    print(fa)
    m = fa.minimize()
    print('Minimized FA')
    print(m)


def test_FA_Minimization():
    infile = utils.promptFile(
        "FA to be minimized (e.g %s) [OPTIONAL]: " % IN_FNAME,
        optional=True)
    if infile == "":
        infile = IN_FNAME

    utils.startTestMsg(msgFAMinimization)
    tFA_Minimization()
