from utils import startTestMsg

from tests.test_FA_Determinization import tFA_Determinization
from tests.test_FA_Minimization import tFA_Minimization
from tests.test_FA_Recognition import tFA_Recognition
from tests.test_FA_Operations import tFA_Renaming_States, tFA_Union
from tests.test_CFG_disk import testCFGReading, testCFGWriting
from tests.test_RegularConversions import *


def test_FA():
    print('\tTesting Determinization\n')
    tFA_Determinization()

    print('\tTesting Minimization\n')
    tFA_Minimization()

    print('\tTesting Words Recognition\n')
    tFA_recognition()

    print('\tTesting Renaming States\n')
    tFA_Renaming_States()

    print('\tTesting Union\n')
    tFA_Union()

def testCFG():
    startTestMsg("TEST CFG READING")
    testCFGReading()

    startTestMsg("TEST CFG WRITING")
    testCFGWriting()


def testRegularConversions():
    startTestMsg("TEST REGULAR GRAMMAR -> FINITE AUTOMATA CONVERSION")
    testRGtoFiniteAutomataConversion()

    startTestMsg("TEST FINITE AUTOMATA -> REGULAR GRAMMAR CONVERSION")
    testFAtoRegularGrammarConversion()

if __name__ == '__main__':
    # test_FA()
    tFA_Union()
    print('\n')
    testCFG()
    print('\n')
    testRegularConversions()
