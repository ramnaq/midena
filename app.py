import sys

from PyQt5.QtWidgets import QApplication
from view.MainWindow import MainWindow
from presenter.MainPresenter import MainPresenter

from model.FileUtil import import_FA


app = QApplication(sys.argv)
view = MainWindow()
presenter = MainPresenter(view)

# Just testing
# fa = import_FA('fa_written.json')
fa = import_FA('tests/primeiroultimo.json')
#fa.sigma = ['a', 'b', 'c']
# fa.export_to('fa_written.json')

print(fa)
# end

view.show()
sys.exit(app.exec_())
