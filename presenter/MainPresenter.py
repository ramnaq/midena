from PyQt5 import QtCore, QtGui, QtWidgets
from presenter.BasePresenter import BasePresenter

from presenter.UIObjectsCreator import production_textEdit, read_productions


class MainPresenter(BasePresenter):
    def __init__(self, view):
        super().__init__(view)
        #singleProdLayout = self.create_production_HLayout()
        #self.view.productions_VLayout.addLayout(singleProdLayout)

    def setup_handlers(self):
        self.view.btn_import_fa.clicked.connect(self.on_import_fa_clicked)
        self.view.btn_create_fa.clicked.connect(self.on_create_fa_clicked)
        self.view.btn_save_fa.clicked.connect(self.on_save_fa_clicked)

        self.view.btn_add_prod.clicked.connect(self.on_add_prod_clicked)
        self.view.btn_remove_prod.clicked.connect(self.on_remove_prod_clicked)
        self.view.btn_create_grammar.clicked.connect(self.on_create_grammar_clicked)
        self.view.btn_remove_grammar.clicked.connect(self.on_remove_grammar_clicked)


    def on_import_fa_clicked(self):
        self.view.set_labeltext("aloha")


    def on_create_fa_clicked(self):
        pass
    

    def on_save_fa_clicked(self):
        pass


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
        grammar = RegularGrammar(symbols, sigma, productions, s, name)


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
