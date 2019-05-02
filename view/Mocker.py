from PyQt5 import QtCore, QtGui, QtWidgets


def mockGrammarTable(view):
    view.addRowToGrammarTable()
    view.ui.grammarTableWidget.setItem(0,2, QtWidgets.QTableWidgetItem("0|0A"))
    view.ui.grammarTableWidget.setItem(0,0, QtWidgets.QTableWidgetItem("S"))
    view.ui.grammarTableWidget.setItem(1,0, QtWidgets.QTableWidgetItem("A"))
    view.ui.grammarTableWidget.setItem(1,2, QtWidgets.QTableWidgetItem("0A|1A|1|0"))

    view.ui.initial_prod_textEdit.setText("S")
    view.ui.symbols_textEdit.setText("S,A,0,1")
    view.ui.terminals_textEdit.setText("0,1")
    view.ui.grammar_name_textEdit.setText("João")

