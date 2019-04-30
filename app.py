import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from view.MainWindow import MainWindow
from presenter.MainPresenter import MainPresenter
from model.FiniteAutomata import FiniteAutomata

app = QApplication(sys.argv)
view = MainWindow()
presenter = MainPresenter(view)

# Just testing
fa = FiniteAutomata.import_from('tests/primeiroultimo.json')
print(fa)
# end

view.show()
sys.exit(app.exec_())
