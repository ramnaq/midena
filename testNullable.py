from model.FileUtil import importGrammar
from model.ContextFreeGrammar import ContextFreeGrammar

g1 = importGrammar('cfgCompleteTest.ext')
g2 = importGrammar('cfgT.ext')

print("original1:\n" + str(g1))
g1.chomskyNormalForm()

print("\n\noriginal2:\n" + str(g2))
g2.chomskyNormalForm()
