import utils

from model.FileUtil import importGrammar, exportGrammar
from model.ContextFreeGrammar import ContextFreeGrammar


msgCFGReading = "TESTING CFG READING"
msgCFGWriting = "TESTING CFG WRITING"

IN_FNAME = "saves/test_CFG.ext"
OUT_FNAME = "saves/test_CFG_exported.ext"

def testCFGReading(fname=IN_FNAME):
    print("Reading " + fname + " Context-Free Grammar...")
    cfg = importGrammar("saves/test_CFG.ext")
    print(str(cfg))

def testCFGWriting(fname=OUT_FNAME):
    cfg = importGrammar(IN_FNAME)
    cfg.name = "CFG_testing"
    print("Writing " + cfg.name + " to " + fname + "...")
    exportGrammar(cfg, fname)
    print("Grammar written!")

def test_CFG_disk():
    infile = utils.promptFile(
            "CFG to be read (e.g %s) [OPTIONAL]: " % IN_FNAME,
            optional=True)
    if infile == "":
        infile = IN_FNAME

    outfile = utils.promptFile(
            "Output file (e.g %s) [OPTIONAL]: " % OUT_FNAME,
            optional=True)
    if outfile == "":
        outfile = OUT_FNAME

    utils.startTestMsg(msgCFGReading)
    testCFGReading(infile)

    print('\n')
    utils.startTestMsg(msgCFGWriting)
    testCFGWriting(outfile)
