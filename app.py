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
fa = FiniteAutomata.import_from('fa_written.json')
#fa = FiniteAutomata.import_from('tests/primeiroultimo.json')
#fa.sigma = ['a', 'b', 'c']
#fa.export_to('fa_written.json')

print(fa)
# end

view.show()
sys.exit(app.exec_())
