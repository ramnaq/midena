from PyQt5 import QtCore, QtGui, QtWidgets


def production_textEdit():
    prodFont = QtGui.QFont()
    prodFont.setPointSize(12)

    prod_textEdit = QtWidgets.QTextEdit()
    prod_textEdit.setMaximumSize(QtCore.QSize(16777215, 25))
    prod_textEdit.setFont(prodFont)
    prod_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    return prod_textEdit
