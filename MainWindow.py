import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import MainPresenter

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/main_window.ui', self)
        
        self.setWindowTitle('Midena')

    def set_presenter(self, presenter):
        self.btn_import_fa.clicked.connect(presenter.on_import_fa_clicked)

    def set_labeltext(self, txt):
        self.btn_create_fa.setText(txt)

    

