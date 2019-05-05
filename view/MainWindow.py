import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from ui.main_window import Ui_MainWindow
from model.FiniteAutomata import FiniteAutomata
from view.Mocker import mockGrammarTable


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setTableItemFont()
        self.setupGrammarTable()
        mockGrammarTable(self)

    def setTableItemFont(self):
        self.tableItemFont = QtGui.QFont()
        self.tableItemFont.setPointSize(18)
        self.tableItemFont.setWeight(50)

    def setupGrammarTable(self):
        self.ui.grammarTableWidget.setColumnCount(3)
        self.ui.grammarTableWidget.setRowCount(1)
        self.ui.grammarTableWidget.setHorizontalHeaderLabels(["α", "→", "ß"])
        self.addArrowToRow(self.ui.grammarTableWidget.currentRow() + 1)

    def addRowToGrammarTable(self):
        itemAlpha = QtWidgets.QTableWidgetItem()
        itemBeta = QtWidgets.QTableWidgetItem()
        itemAlpha.setFont(self.tableItemFont)
        itemBeta.setFont(self.tableItemFont)

        row = self.ui.grammarTableWidget.rowCount()
        self.ui.grammarTableWidget.setRowCount(row + 1)
        self.ui.grammarTableWidget.setItem(row + 1, 0, itemAlpha)
        self.ui.grammarTableWidget.setItem(row + 1, 2, itemBeta)
        self.addArrowToRow(row)

    def addArrowToRow(self, row):
        arrowItem = QtWidgets.QTableWidgetItem("   →")
        arrowItem.setFlags(QtCore.Qt.NoItemFlags)
        arrowItem.setFlags(QtCore.Qt.ItemIsEnabled)
        arrowItem.setFont(self.tableItemFont)

        self.ui.grammarTableWidget.setItem(row, 1, arrowItem)

    def addGrammarToListBox(self, g):
        self.ui.grammarsWidgetList.addItem(QtWidgets.QListWidgetItem(g.name))

    def clearGrammarFields(self):
        self.ui.initial_prod_textEdit.setText("")
        self.ui.symbols_textEdit.setText("")
        self.ui.terminals_textEdit.setText("")
        self.ui.grammar_name_textEdit.setText("")
        self.ui.grammarTableWidget.setRowCount(0)
        self.setupGrammarTable()

    def set_labeltext(self, txt):
        self.ui.btn_create_fa.setText(txt)

    def add_listener(self, presenter):
        self.ui.btn_import_fa.clicked.connect(presenter.on_import_fa_clicked)
        self.ui.btn_create_fa.clicked.connect(presenter.on_create_fa_clicked)
        self.ui.btn_save_fa.clicked.connect(presenter.on_save_fa_clicked)

        self.ui.btn_add_prod.clicked.connect(presenter.on_add_prod_clicked)
        self.ui.btn_remove_prod.clicked.connect(presenter.on_remove_prod_clicked)
        self.ui.btn_create_grammar.clicked.connect(presenter.on_create_grammar_clicked)
        self.ui.btn_remove_grammar.clicked.connect(presenter.on_remove_grammar_clicked)
        self.ui.exportGrammarBtn.clicked.connect(presenter.onExportGrammarBtnClicked)
        self.ui.importGrammarBtn.clicked.connect(presenter.onImportGrammarBtnClicked)

    def show_FA(self, fa: FiniteAutomata):
        sigma = {}
        for i, s in enumerate(sorted(fa.sigma)):
            sigma[i] = s

        states_label = []
        for s in fa.states():
            label = s
            if (s in fa.accepting):
                label = '* ' + label 
            if (s in fa.initial):
                label = '> ' + label
            states_label.append(label)

        self.ui.tableWidget.setColumnCount(len(sigma))
        self.ui.tableWidget.setRowCount(len(states_label))
        self.ui.tableWidget.setVerticalHeaderLabels(states_label)
        self.ui.tableWidget.setHorizontalHeaderLabels(sigma.values())

        for i, state in enumerate(fa.states()):
            for j, symbol in sigma.items():
                if symbol in fa.table[state]:
                    self.ui.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(
                            str(fa.table[state][symbol]))
                    )

    def showGrammar(self, g):
        pass

