from model.FileUtil import importGrammar
from model.ContextFreeGrammar import ContextFreeGrammar

g = importGrammar('cfgTestSimple.ext')
print("original:\n" + str(g))
g.chomskyNormalForm()
print("modified:\n" + str(g))
