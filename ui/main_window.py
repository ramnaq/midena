# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 290, 530))
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
        self.btn_convert_fa_gr.setGeometry(QtCore.QRect(10, 280, 120, 30))
        self.btn_convert_fa_gr.setObjectName("btn_convert_fa_gr")
        self.btn_save_fa = QtWidgets.QPushButton(self.groupBox)
        self.btn_save_fa.setGeometry(QtCore.QRect(210, 30, 70, 30))
        self.btn_save_fa.setFlat(False)
        self.btn_save_fa.setObjectName("btn_save_fa")
        self.btn_determinize_fa = QtWidgets.QPushButton(self.groupBox)
        self.btn_determinize_fa.setGeometry(QtCore.QRect(10, 320, 120, 30))
        self.btn_determinize_fa.setObjectName("btn_determinize_fa")
        self.btn_minimize_fa = QtWidgets.QPushButton(self.groupBox)
        self.btn_minimize_fa.setGeometry(QtCore.QRect(140, 320, 100, 30))
        self.btn_minimize_fa.setObjectName("btn_minimize_fa")
        self.btn_convert_fa_regex = QtWidgets.QPushButton(self.groupBox)
        self.btn_convert_fa_regex.setGeometry(QtCore.QRect(140, 280, 140, 30))
        self.btn_convert_fa_regex.setObjectName("btn_convert_fa_regex")
        self.btn_view_fa = QtWidgets.QPushButton(self.groupBox)
        self.btn_view_fa.setGeometry(QtCore.QRect(10, 360, 120, 30))
        self.btn_view_fa.setObjectName("btn_view_fa")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(310, 10, 290, 530))
        self.groupBox_2.setFlat(False)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(610, 10, 280, 250))
        self.groupBox_3.setFlat(False)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(610, 270, 280, 270))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 22))
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
        self.btn_view_fa.setText(_translate("MainWindow", "View FA"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Grammar"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Regular Expression"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Tests"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))

