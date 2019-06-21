from model.FileUtil import importGrammar
from model.ContextFreeGrammar import ContextFreeGrammar

g = importGrammar('g.ext')
g.chomskyNormalForm()
