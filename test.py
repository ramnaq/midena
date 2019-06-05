import os.path

from sys import argv

from tests.test_CFG_disk import *
from tests.test_FA_Operations import *
from tests.test_FA_Recognition import *
from tests.test_FA_Minimization import *
from tests.test_RegularConversions import *
from tests.test_FA_Determinization import *


if len(argv) < 3 or argv[1] != "-t":
    print("Usage: python test.py -t <testFile>")
    exit()
else:
    func_name = argv[2]
    if not os.path.isfile("tests/" + func_name + ".py"):
        raise NotImplementedError("Test file %s not found!" % func_name)

    possibles = globals().copy()
    possibles.update(locals())
    function = possibles.get(func_name)
    if not function:
        raise NotImplementedError("Function %s not implemented" % func_name)
    function()
