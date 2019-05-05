# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(905, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 290, 641))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 270, 200))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.btn_create_fa = QtWidgets.QPushButton(self.groupBox)
        self.btn_create_fa.setGeometry(QtCore.QRect(10, 30, 90, 30))
        self.btn_create_fa.setFlat(False)
        self.btn_create_fa.setObjectName("btn_create_fa")
        self.btn_import_fa = QtWidgets.QPushButton(self.groupBox)
        self.btn_import_fa.setGeometry(QtCore.QRect(110, 30, 90, 30))
        self.btn_import_fa.setFlat(False)
        self.btn_import_fa.setObjectName("btn_import_fa")
        self.btn_convert_fa_gr = QtWidgets.QPushButton(self.groupBox)
        self.btn_convert_fa_gr.setGeometry(QtCore.QRect(10, 280, 100, 30))
        self.btn_convert_fa_gr.setObjectName("btn_convert_fa_gr")
        self.btn_save_fa = QtWidgets.QPushButton(self.groupBox)
        self.btn_save_fa.setGeometry(QtCore.QRect(210, 30, 70, 30))
        self.btn_save_fa.setFlat(False)
        self.btn_save_fa.setObjectName("btn_save_fa")
        self.btn_determinize_fa = QtWidgets.QPushButton(self.groupBox)
        self.btn_determinize_fa.setGeometry(QtCore.QRect(10, 320, 100, 30))
        self.btn_determinize_fa.setObjectName("btn_determinize_fa")
        self.btn_minimize_fa = QtWidgets.QPushButton(self.groupBox)
        self.btn_minimize_fa.setGeometry(QtCore.QRect(120, 320, 100, 30))
        self.btn_minimize_fa.setObjectName("btn_minimize_fa")
        self.btn_convert_fa_regex = QtWidgets.QPushButton(self.groupBox)
        self.btn_convert_fa_regex.setGeometry(QtCore.QRect(120, 280, 120, 30))
        self.btn_convert_fa_regex.setObjectName("btn_convert_fa_regex")
        self.GrammarGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.GrammarGroupBox.setGeometry(QtCore.QRect(310, 10, 290, 641))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.GrammarGroupBox.setFont(font)
        self.GrammarGroupBox.setFlat(False)
        self.GrammarGroupBox.setObjectName("GrammarGroupBox")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.GrammarGroupBox)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 27, 276, 531))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grammar_creation_VLayout = QtWidgets.QVBoxLayout()
        self.grammar_creation_VLayout.setObjectName("grammar_creation_VLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.initialProdLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.initialProdLabel.setObjectName("initialProdLabel")
        self.horizontalLayout_4.addWidget(self.initialProdLabel)
        self.initial_prod_textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.initial_prod_textEdit.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.initial_prod_textEdit.setFont(font)
        self.initial_prod_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.initial_prod_textEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.initial_prod_textEdit.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.initial_prod_textEdit.setObjectName("initial_prod_textEdit")
        self.horizontalLayout_4.addWidget(self.initial_prod_textEdit)
        self.grammar_creation_VLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.symbolsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.symbolsLabel.setObjectName("symbolsLabel")
        self.horizontalLayout_5.addWidget(self.symbolsLabel)
        self.symbols_textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.symbols_textEdit.sizePolicy().hasHeightForWidth())
        self.symbols_textEdit.setSizePolicy(sizePolicy)
        self.symbols_textEdit.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.symbols_textEdit.setFont(font)
        self.symbols_textEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.symbols_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.symbols_textEdit.setObjectName("symbols_textEdit")
        self.horizontalLayout_5.addWidget(self.symbols_textEdit)
        self.grammar_creation_VLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.terminalsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.terminalsLabel.setObjectName("terminalsLabel")
        self.horizontalLayout_10.addWidget(self.terminalsLabel)
        self.terminals_textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.terminals_textEdit.setMaximumSize(QtCore.QSize(110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.terminals_textEdit.setFont(font)
        self.terminals_textEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.terminals_textEdit.setObjectName("terminals_textEdit")
        self.horizontalLayout_10.addWidget(self.terminals_textEdit)
        self.grammar_creation_VLayout.addLayout(self.horizontalLayout_10)
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.grammar_creation_VLayout.addWidget(self.line)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.prodsLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.prodsLabel.setObjectName("prodsLabel")
        self.horizontalLayout_12.addWidget(self.prodsLabel)
        self.btn_add_prod = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_add_prod.setObjectName("btn_add_prod")
        self.horizontalLayout_12.addWidget(self.btn_add_prod)
        self.btn_remove_prod = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_remove_prod.setObjectName("btn_remove_prod")
        self.horizontalLayout_12.addWidget(self.btn_remove_prod)
        self.grammar_creation_VLayout.addLayout(self.horizontalLayout_12)
        self.grammarTableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget_3)
        self.grammarTableWidget.setObjectName("grammarTableWidget")
        self.grammarTableWidget.setColumnCount(0)
        self.grammarTableWidget.setRowCount(0)
        self.grammar_creation_VLayout.addWidget(self.grammarTableWidget)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.grammar_name_textEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget_3)
        self.grammar_name_textEdit.setMaximumSize(QtCore.QSize(110, 25))
        self.grammar_name_textEdit.setToolTip("")
        self.grammar_name_textEdit.setStatusTip("")
        self.grammar_name_textEdit.setWhatsThis("")
        self.grammar_name_textEdit.setAccessibleName("")
        self.grammar_name_textEdit.setAccessibleDescription("")
        self.grammar_name_textEdit.setObjectName("grammar_name_textEdit")
        self.horizontalLayout_11.addWidget(self.grammar_name_textEdit)
        self.btn_create_grammar = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_create_grammar.setMinimumSize(QtCore.QSize(0, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_create_grammar.setFont(font)
        self.btn_create_grammar.setObjectName("btn_create_grammar")
        self.horizontalLayout_11.addWidget(self.btn_create_grammar)
        self.grammar_creation_VLayout.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2.addLayout(self.grammar_creation_VLayout)
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget_3)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.grammarListLabel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.grammarListLabel.setFont(font)
        self.grammarListLabel.setObjectName("grammarListLabel")
        self.verticalLayout_2.addWidget(self.grammarListLabel)
        self.grammarsWidgetList = QtWidgets.QListWidget(self.verticalLayoutWidget_3)
        self.grammarsWidgetList.setObjectName("grammarsWidgetList")
        item = QtWidgets.QListWidgetItem()
        self.grammarsWidgetList.addItem(item)
        self.verticalLayout_2.addWidget(self.grammarsWidgetList)
        self.btn_remove_grammar = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.btn_remove_grammar.setObjectName("btn_remove_grammar")
        self.verticalLayout_2.addWidget(self.btn_remove_grammar)
        self.exportGrammarBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.exportGrammarBtn.setObjectName("exportGrammarBtn")
        self.verticalLayout_2.addWidget(self.exportGrammarBtn)
        self.importGrammarBtn = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.importGrammarBtn.setObjectName("importGrammarBtn")
        self.verticalLayout_2.addWidget(self.importGrammarBtn)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(610, 10, 280, 301))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(610, 320, 280, 331))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 905, 20))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Automata"))
        self.btn_create_fa.setText(_translate("MainWindow", "Create New"))
        self.btn_import_fa.setText(_translate("MainWindow", "Import FA"))
        self.btn_convert_fa_gr.setText(_translate("MainWindow", "Convert to RG"))
        self.btn_save_fa.setText(_translate("MainWindow", "Save FA"))
        self.btn_determinize_fa.setText(_translate("MainWindow", "Determinize"))
        self.btn_minimize_fa.setText(_translate("MainWindow", "Minimize"))
        self.btn_convert_fa_regex.setText(_translate("MainWindow", "Convert to Reg Exp"))
        self.GrammarGroupBox.setTitle(_translate("MainWindow", "Grammar"))
        self.initialProdLabel.setText(_translate("MainWindow", "Initital "))
        self.symbolsLabel.setText(_translate("MainWindow", "Symbols"))
        self.terminalsLabel.setText(_translate("MainWindow", "Terminal Symbols   "))
        self.prodsLabel.setText(_translate("MainWindow", "Productions"))
        self.btn_add_prod.setText(_translate("MainWindow", "Add"))
        self.btn_remove_prod.setText(_translate("MainWindow", "Remove"))
        self.btn_create_grammar.setText(_translate("MainWindow", "Create Grammar"))
        self.grammarListLabel.setText(_translate("MainWindow", "List of Grammars"))
        __sortingEnabled = self.grammarsWidgetList.isSortingEnabled()
        self.grammarsWidgetList.setSortingEnabled(False)
        item = self.grammarsWidgetList.item(0)
        item.setText(_translate("MainWindow", "[Regular Grammar example] (0(0+1)*)"))
        self.grammarsWidgetList.setSortingEnabled(__sortingEnabled)
        self.btn_remove_grammar.setText(_translate("MainWindow", "Remove"))
        self.exportGrammarBtn.setText(_translate("MainWindow", "Export"))
        self.importGrammarBtn.setText(_translate("MainWindow", "Import"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Regular Expression"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Tests"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))


