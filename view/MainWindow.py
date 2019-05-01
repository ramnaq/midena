import sys

from PyQt5 import QtWidgets
from ui.main_window import Ui_MainWindow
from model.FiniteAutomata import FiniteAutomata


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def set_labeltext(self, txt):
        self.ui.btn_create_fa.setText(txt)

    def add_listener(self, presenter):
        self.ui.btn_import_fa.clicked.connect(presenter.on_import_fa_clicked)
        self.ui.btn_create_fa.clicked.connect(presenter.on_create_fa_clicked)
        self.ui.btn_save_fa.clicked.connect(presenter.on_save_fa_clicked)

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
