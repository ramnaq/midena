from model.FileUtil import importGrammar, exportGrammar
from model.ContextFreeGrammar import ContextFreeGrammar


inFileName = "saves/test_CFG.ext"
outFileName = "saves/test_CFG_exported.ext"

def testCFGReading():
    print("Reading " + inFileName + " Context-Free Grammar...")
    cfg = importGrammar("saves/test_CFG.ext")
    print(str(cfg))

def testCFGWriting():
    cfg = importGrammar(inFileName)
    cfg.name = "CFG_testing"
    print("Writing " + cfg.name + " to " + outFileName + "...")
    exportGrammar(cfg, outFileName)
    print("Grammar written!")

