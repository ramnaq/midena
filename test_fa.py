from model.FileUtil import import_FA

if __name__ == '__main__':
    fa = import_FA('saves/equal_first_last.json')
    print(fa)
    m = fa.minimize()
    print(m)
