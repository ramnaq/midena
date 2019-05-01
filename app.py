import sys

from PyQt5.QtWidgets import QApplication
from view.MainWindow import MainWindow
from presenter.MainPresenter import MainPresenter

app = QApplication(sys.argv)
view = MainWindow()
presenter = MainPresenter(view)
view.add_listener(presenter)
view.show()
sys.exit(app.exec_())
