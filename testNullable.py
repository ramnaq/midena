from model.FileUtil import importGrammar
from model.ContextFreeGrammar import ContextFreeGrammar

g = importGrammar('cfgTest.ext')
g.chomskyNormalForm()
