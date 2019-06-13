from PyQt5 import QtCore, QtGui, QtWidgets

from model.FileUtil import *
from model.RegularExpression import RegularExpression
from model.regular_obj_conversion import *
from presenter.BasePresenter import BasePresenter
from presenter.UIObjectsCreator import *


class MainPresenter(BasePresenter):

    def __init__(self, view):
        super().__init__(view)
        self.grammars = []

    def onCreateFAClicked(self):
        self.current_fa = None

    def onImportFA(self, path):
        self.current_fa = import_FA(path)
        self.view.showFA(self.current_fa)

    def onSaveFAClicked(self):
        if self.current_fa is not None:
            export_FA(self.current_fa, "tests/other_fa.json")

    def onAddProdClicked(self):
        self.view.addRowToGrammarTable()

    def onRemoveProductionClicked(self):
        n = self.view.ui.grammarTableWidget.rowCount()
        self.view.ui.grammarTableWidget.setRowCount(n-1)

    def onConvertFAtoRGBtnClicked(self):
        if self.current_fa is not None:
            grammar = finite_automata_to_grammar(self.current_fa)
            self.view.showGrammar(grammar)

    def onCreateGrammarClicked(self):
        s = self.view.ui.initial_prod_textEdit.toPlainText()
        symbols_entry = self.view.ui.symbols_textEdit.toPlainText()
        symbols = set(symbols_entry.split(','))
        terminals_entry = self.view.ui.terminals_textEdit.toPlainText()
        sigma = set(terminals_entry.split(','))
        name = self.view.ui.grammar_name_textEdit.toPlainText()

        grammar = None
        try:
            productions = read_productions(self.view.ui.grammarTableWidget)
            grammar = createGrammar(symbols, sigma, productions, s, name)
            self.view.addGrammarToListBox(grammar)
        except(ValueError):
            ...

        self.view.clearGrammarFields()
        self.grammars.append(grammar)
        return grammar

    def on_remove_grammar_clicked(self):
        selectedGrammar = self.view.ui.grammarsWidgetList.currentItem()
        row = self.view.ui.grammarsWidgetList.row(selectedGrammar)
        self.view.ui.grammarsWidgetList.takeItem(row)

    def onExportGrammarBtnClicked(self):
        selectedGrammar = self.view.ui.grammarsWidgetList.currentItem()
        if (selectedGrammar is not None):
            name = selectedGrammar.text()
            grammar = self.findByName(name)
            if grammar is not None:
                parent = self.view.ui.centralwidget
                fileName = promptFileName(parent,
                        'Export grammar to file',
                        'Enter the file name:')
                exportGrammar(grammar, fileName)
        else:
            showWarning(
                    "Please, select in the list the grammar to be exported.")

    def onImportGrammarBtnClicked(self):
        parent = self.view.ui.centralwidget
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                parent,
                'Open file', "Midena Files (*.ext *.json)")
        if fileName != "":
            grammar = importGrammar(fileName)
            self.view.showGrammar(grammar)

    def onGrammarToFABtnClicked(self):
        selectedGrammar = self.view.ui.grammarsWidgetList.currentItem()
        if (selectedGrammar is not None):
            name = selectedGrammar.text()
            grammar = self.findByName(name)
            if (grammar is not None) and (grammar.type == 3):
                fa = rg_to_fa(grammar)
                self.view.showFA(fa)
            else:
                showWarning("The grammar must be of type 3 (a Regular Grammar)")
        else:
            showWarning(
                    "Please, select in the list the grammar to be converted")


    def onExportRegExBtnClicked(self):
        parent = self.view.ui.centralwidget
        fileName = promptFileName(parent, 'Export regular expression to file',
                                  'Enter the file name:')

        regexStr = self.view.ui.regExTextEdit.toPlainText()
        # validate if regexStr is a valid regular expression with specific
        # automata (maybe in RegularExpression constructor)
        regex = RegularExpression(regexStr)
        exportRegEx(regex, fileName)
        self.view.clearRegExField()

    def onImportRegExBtnClicked(self):
        parent = self.view.ui.centralwidget
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                parent,
                'Open file',
                "Midena Files (*.ext *.json)")
        if fileName != "":
            regex = importRegEx(fileName)
            self.view.showRegEx(regex)

    def findByName(self, name):
        for g in self.grammars:
            if g.name == name:
                return g
        return None

    def on_save_fa(self, path: str):
        if self.current_fa is not None:
            self.current_fa.name = path.split('/')[-1].replace('.json', '')
            export_FA(self.current_fa, path)

    def on_fa_item_changed(self, updated_fa):
        try:
            self.current_fa = updated_fa
            self.view.showFA(updated_fa)
        except Exception as exc:
            print(f'Exception: {exc}')

    def on_determinize_fa(self):
        if self.current_fa.is_dfa():
            print('Current automata is already Deterministic.')
        else:
            self.on_fa_item_changed(self.current_fa.determinize())

    def on_minimize_fa(self):
        self.on_fa_item_changed(self.current_fa.minimize())

    def on_test_word(self, text: str):
        if not self.current_fa:
            print("Error: No FA active")
            return
        accept = self.current_fa.accept(text)
        self.view.show_test_word_msg('accepted' if accept else 'rejected')
