from PyQt5 import QtCore, QtGui, QtWidgets


def production_textEdit():
    prodFont = QtGui.QFont()
    prodFont.setPointSize(12)

    prod_textEdit = QtWidgets.QTextEdit()
    prod_textEdit.setMaximumSize(QtCore.QSize(16777215, 25))
    prod_textEdit.setFont(prodFont)
    prod_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

    return prod_textEdit


def read_productions(tableWidget):
    productions = []
    for i in range(tableWidget.rowCount()):
        alpha_entry = tableWidget.item(i,0)
        beta_entry = tableWidget.item(i,2)
        if (alpha_entry is not None) and (beta_entry is not None):
            if (alpha_entry.text() != "") and (beta_entry.text() != ""):
                alpha = alpha_entry.text()
                if alpha != "":
                    beta = beta_entry.text().split('|')
                    productions.append((alpha, beta))
            else:
                raise ValueError("Neither α or ß can be empty!")
        else:
            raise ValueError("Item must not be None!")
    return productions


def promptFileName(parent, promptName, text):
    filename = ""
    fileNameEntry, selectedFilter = QtWidgets.QFileDialog.getSaveFileName(parent, "Save F:xile")
    if fileNameEntry[-4:] != ".ext":
        filename = fileNameEntry + ".ext"
    else:
        filename = fileNameEntry
    return filename
