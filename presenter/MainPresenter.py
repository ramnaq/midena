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
        self.view.addRowToGrammarTable()

    def on_remove_prod_clicked(self):
        pass

    def on_create_grammar_clicked(self):
        s = self.view.ui.initial_prod_textEdit.toPlainText()
        symbols_entry = self.view.ui.symbols_textEdit.toPlainText()
        symbols = set(symbols_entry.split(','))
        terminals_entry = self.view.ui.terminals_textEdit.toPlainText()
        sigma = set(terminals_entry.split(','))
        name = self.view.ui.grammar_name_textEdit.toPlainText()

        grammar = None
        try:
            productions = read_productions(self.view.ui.grammarTableWidget)
            grammar = RegularGrammar(symbols, sigma, productions, s, name)
            self.view.addGrammarToListBox(grammar)
        except(ValueError):
            ...

        self.view.clearGrammarFields()
        return grammar

    def on_remove_grammar_clicked(self):
        pass

