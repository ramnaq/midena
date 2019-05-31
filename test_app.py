from tests.test_FA_Determinization import tFA_Determinization
from tests.test_FA_Minimization import tFA_Minimization
from tests.test_FA_recognition import tFA_recognition
from tests.test_FA_Operations import tFA_Renaming_States, tFA_Union


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


if __name__ == '__main__':
    # test_FA()
    tFA_Union()
