from model.FileUtil import import_FA


def tFA_Minimization():
    fa = import_FA('saves/test_minimization.json')
    print('Original FA')
    print(fa)
    m = fa.minimize()
    print('Minimized FA')
    print(m)
