import sys

from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

# from view.BaseView import BaseView

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi('ui/main_window.ui', self)
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Midena')

    def set_labeltext(self, txt):
        self.btn_create_fa.setText(txt)

    

