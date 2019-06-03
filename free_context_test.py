import os
from model.FileUtil import importGrammar, exportGrammar

print("Importing grammar...")
fcg = importGrammar("/home/sidharta/workspace/midena/tests/CFG_example.ext")

print("Exporting grammar in CFG_example2.ext")
exportGrammar(fcg, "/home/sidharta/workspace/midena/tests/CFG_example2.ext")

