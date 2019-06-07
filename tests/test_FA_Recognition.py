import utils

from model.FileUtil import import_FA


msgFARecognition = "TESTING FA RECOGNITION"

IN_FNAME1 = "saves/test_FA_equalFirstLast.ext"
#IN_FNAME2 = "saves/test_Nfa_ends_with_zero.ext"

def xtest(dfa, words, expected, msg='Success!', start=0):
    i = start
    for word in words:
        i += 1
        if dfa.accept(word) == expected:
            print(f'Test {i}: OK ({word})')
        else:
            print(f'Test {i} failed with word: {word}')
            print(f'Expected: {"accept" if expected else "not accept"}\n')
    print(f'{msg}\n')


def tFA_Recognition(fname1=IN_FNAME1):
    # starts and ends with same symbol
    dfa = import_FA(fname1)
    print(dfa)

    right_words = ['', 'a', 'b', 'aa', 'bb', 'aabbaba', 'bababab', 'bbbab']
    xtest(dfa, right_words, True, msg='Correct words accepted.')

    wrong_words = ['ab', 'ba', 'abcba', 'c', 'ababbbab', 'bbabbabbabababa']
    xtest(dfa, wrong_words, False, msg='Wrong words correctly not accepted.',
          start=len(right_words))

    # ends with 0 (zero)
    #dfa = import_FA(fname2)
    #print(dfa)

    #right_words = ['0', '000', '01010', '11110', '10', '11110', '10101010']
    #xtest(dfa, right_words, True, msg='Correct words accepted.')

    #wrong_words = ['1', '01', '0001', '101', '11101', '01010101', '101010101']
    #xtest(dfa, wrong_words, False, msg='Wrong words correctly not accepted.',
    #      start=len(right_words))

def test_FA_Recognition():
    infile1 = utils.promptFile(
            "FA to be recognized (e.g %s) [OPTIONAL]: " % IN_FNAME1,
            optional=True)
    if infile1 == "":
        infile1 = IN_FNAME1

    #infile2 = utils.promptFile(
    #        "FA1 to do union (e.g %s) [OPTIONAL]: " % IN_FNAME2,
    #        optional=True)
    #if infile2 == "":
    #    infile2= IN_FNAME2

    utils.startTestMsg(msgFARecognition)
    tFA_Recognition(infile1)
