import sys

from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
from MainPresenter import MainPresenter

app = QApplication(sys.argv)
view = MainWindow()
presenter = MainPresenter(view)
view.set_presenter(presenter)
view.show()
sys.exit(app.exec_())