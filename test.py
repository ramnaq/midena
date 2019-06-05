import os.path

from sys import argv

from tests.test_CFG_disk import *
from tests.test_FA_Operations import *
from tests.test_FA_Recognition import *
from tests.test_FA_Minimization import *
from tests.test_RegularConversions import *
from tests.test_FA_Determinization import *

err = "[ERROR]"

if len(argv) < 3 or argv[1] != "-t":
    print("Usage: python test.py -t <test_name>.\n")
    print("Example: python test.py -t test_FA_Operations")
    exit()
else:
    possibles = globals().copy()
    possibles.update(locals())

    for arg in argv[2:]:
        print("T E S T  " + arg + "\n")
        func_name = arg
        if not os.path.isfile("tests/" + func_name + ".py"):
            print("%s Test file %s not found!" % err % func_name)
        else:
            function = possibles.get(func_name)
            if not function:
                print("%s Functions %s not implemented" % err % func_name)
            else:
                function()
                print("\n")
