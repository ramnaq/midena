from PyQt5 import QtCore, QtGui, QtWidgets


def production_textEdit():
    prodFont = QtGui.QFont()
    prodFont.setPointSize(12)

    prod_textEdit = QtWidgets.QTextEdit()
    prod_textEdit.setMaximumSize(QtCore.QSize(16777215, 25))
    prod_textEdit.setFont(prodFont)
    prod_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    return prod_textEdit


def read_productions(prods_VLayout):
    prods_HLayouts = [prods_VLayout.itemAt(i) for i in range(prods_VLayout.count())]
    productions = []
    for p_layout in prods_HLayouts:
        prods_objs = [p_layout.itemAt(i) for i in range(p_layout.count())]
        print(prods_objs[0])
        alpha = p_layout.itemAt(0).toPlainText()
        beta = p_layout.itemAt(2).toPlainText().split('|')
        productions.append((alpha, beta))
    return productions
