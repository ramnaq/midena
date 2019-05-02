from PyQt5 import QtCore, QtGui, QtWidgets


def production_textEdit():
    prodFont = QtGui.QFont()
    prodFont.setPointSize(12)

    prod_textEdit = QtWidgets.QTextEdit()
    prod_textEdit.setMaximumSize(QtCore.QSize(16777215, 25))
    prod_textEdit.setFont(prodFont)
    prod_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    return prod_textEdit


def read_productions(tableWidget):
    productions = []
    for i in range(tableWidget.rowCount()):
        alpha = tableWidget.item(i,0).text()
        beta = tableWidget.item(i,2).text().split('|')
        productions.append((alpha, beta))
    return productions
