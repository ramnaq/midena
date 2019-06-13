import utils

from model.FileUtil import import_FA


msgFADeterminization = "TESTING FA DETERMINIZATION"

IN_FNAME = "saves/test_Determinization.ext"

def tFA_Determinization(fname=IN_FNAME):
    fa = import_FA(fname)
    print('Original NFA')
    print(fa)
    m = fa.determinize()
    print('Determinized FA')
    print(m)

def test_FA_Determinization():
    infile = utils.promptFile(
            "FA to be determinized (e.g %s) [OPTIONAL]: " % IN_FNAME,
            optional=True)
    if infile == "":
        infile = IN_FNAME

    utils.startTestMsg(msgFADeterminization)
    tFA_Determinization(infile)
