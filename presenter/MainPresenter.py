from PyQt5 import QtCore, QtGui, QtWidgets

from presenter.BasePresenter import BasePresenter
from model.FileUtil import import_FA, export_FA
from presenter.UIObjectsCreator import production_textEdit, read_productions
from model.RegularGrammar import RegularGrammar


class MainPresenter(BasePresenter):

    def __init__(self, view):
        super().__init__(view)
        # singleProdLayout = self.create_production_HLayout()
        # self.view.productions_VLayout.addLayout(singleProdLayout)

    def on_create_fa_clicked(self):
        pass

    def on_import_fa_clicked(self):
        self.current_fa = import_FA('tests/primeiroultimo.json')
        self.view.show_FA(self.current_fa)

    def on_save_fa_clicked(self):
        if self.current_fa is not None:
            export_FA(self.current_fa, "tests/other_fa.json")

    def on_add_prod_clicked(self):
        prodLayout = self.create_production_HLayout()
        self.view.productions_VLayout.addLayout(prodLayout)

    def on_remove_prod_clicked(self):
        pass

    def on_create_grammar_clicked(self):
        s = self.view.initial_prod_textEdit.toPlainText()
        symbols_entry = self.view.symbols_textEdit.toPlainText()
        terminals_entry = self.view.terminals_textEdit.toPlainText()
        name = self.view.grammar_name_textEdit.toPlainText()
        productions = read_productions(self.view.productions_VLayout)

        symbols = set(symbols_entry.split(','))
        sigma = set(terminals_entry.split(','))
        self.grammar = RegularGrammar(symbols, sigma, productions, s, name)

    def on_remove_grammar_clicked(self):
        pass

    def create_production_HLayout(self):
        prodLayout = QtWidgets.QHBoxLayout()

        alphaTextEdit = production_textEdit()
        betaTextEdit = production_textEdit()

        arrowFont = QtGui.QFont()
        arrowFont.setPointSize(18)
        arrowFont.setWeight(50)

        arrow = QtWidgets.QLabel("→")
        arrow.setMaximumSize(QtCore.QSize(16777215, 30))
        arrow.setFont(arrowFont)

        prodLayout.addWidget(alphaTextEdit)
        prodLayout.addWidget(arrow)
        prodLayout.addWidget(betaTextEdit)

        return prodLayout
