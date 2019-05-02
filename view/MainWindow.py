from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSignal


from ui.main_window import Ui_MainWindow
from model.FiniteAutomata import FiniteAutomata


class MainWindow(QtWidgets.QMainWindow):

    faItemChanged = pyqtSignal(FiniteAutomata)
    faImport = pyqtSignal(str)
    faSave = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def set_labeltext(self, txt):
        self.ui.btn_create_fa.setText(txt)

    def add_listener(self, presenter):
        self.ui.btn_create_fa.clicked.connect(self.on_create_fa_clicked)
        self.ui.btn_import_fa.clicked.connect(self.on_import_fa_clicked)
        self.ui.btn_save_fa.clicked.connect(self.on_save_fa_clicked)

        self.ui.tableWidget.itemDoubleClicked.connect(self.on_fa_item_selected)
        self.ui.tableWidget.itemChanged.connect(self.on_fa_item_changed)
        
        self.faImport.connect(presenter.on_import_fa)
        self.faSave.connect(presenter.on_save_fa)
        self.faItemChanged.connect(presenter.on_fa_item_changed)

    def on_create_fa_clicked(self):
        num_states, ok = QtWidgets.QInputDialog.getInt(
            self, "States", "Number of states:", 4, 1, 20, 1
        )
        if not ok:
            return
        
        num_sigma, okSigma = QtWidgets.QInputDialog.getInt(
            self, "Sigma", "Number of symbols:", 2, 1, 20, 1
        )
        if not okSigma:
            return
        
        sigma = [chr(i) for i in range(97, 97 + num_sigma)]
        table = {}
        for i in range(num_states):
            table['q' + str(i)] = {x: '-' for x in sigma}
        initial = 'q0'
        accepting = ['q' + str(num_states - 1)]
        self.current_fa = FiniteAutomata(sigma, table, initial, accepting)
        self.faItemChanged.emit(self.current_fa)

    def on_import_fa_clicked(self):
        path, _ = QtWidgets.QFileDialog.getOpenFileName(self)
        if path:
            self.faImport.emit(path)

    def on_save_fa_clicked(self):
        if not self.current_fa:
            print("Error: No FA active")
            return

        path, _ = QtWidgets.QFileDialog.getSaveFileName(self)
        if path:
            self.faSave.emit(path)

    def show_FA(self, fa: FiniteAutomata):
        self.ui.tableWidget.blockSignals(True)
        self.ui.tableWidget.clear()
        self.current_fa = fa
        sigma = {}
        for i, s in enumerate(sorted(fa.sigma), 1):
            sigma[i] = s

        states_label = {}
        for s in fa.states():
            label = s
            if (s in fa.accepting):
                label = '* ' + label
            if (s in fa.initial):
                label = '> ' + label
            states_label[s] = label

        self.ui.tableWidget.setColumnCount(len(sigma) + 1)
        self.ui.tableWidget.setRowCount(len(states_label) + 1)

        for i, state in enumerate(fa.states(), 1):
            self.ui.tableWidget.setItem(
                i, 0, QtWidgets.QTableWidgetItem(states_label[state])
            )
            for j, symbol in sigma.items():
                self.ui.tableWidget.setItem(
                    0, j, QtWidgets.QTableWidgetItem(symbol)
                )
                if symbol in fa.table[state]:
                    self.ui.tableWidget.setItem(
                        i, j, QtWidgets.QTableWidgetItem(
                            fa.transition_to_text(fa.table[state][symbol]))
                    )
        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.blockSignals(False)

    def column_to_symbol(self, column):
        return self.ui.tableWidget.item(0, column).text()

    def row_to_state(self, row):
        return self.ui.tableWidget.item(row, 0).text()

    def on_fa_item_selected(self, item):
        self.fa_selected_item = item.text()

    def on_fa_item_changed(self, item):
        if item.row() == 0:
            # add or update sigma symbol
            symbol = item.text()
            self.current_fa.update_sigma(self.fa_selected_item, symbol)
        elif item.column() == 0:
            # add or update state
            st = self.state_from_label(item.text())
            self.current_fa.update_state(self.state_from_label(self.fa_selected_item), st)
            if '*' in item.text():
                if st not in self.current_fa.accepting:
                    self.current_fa.accepting.append(st)
            if '>' in item.text():
                self.current_fa.initial = st
        else:
            # add or update transition
            tr = item.text()
            st = self.state_from_label(self.row_to_state(item.row()))
            symbol = self.column_to_symbol(item.column())
            if tr == '':
                tr = '-'
            self.current_fa.table[st][symbol] = self.current_fa.text_to_transition(tr)
        self.ui.tableWidget.resizeColumnsToContents()
        self.faItemChanged.emit(self.current_fa)

    def state_from_label(self, label: str):
        return label.replace('>', '').replace('*', '').strip()
