# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sign-up.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from bbdd import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(259, 441)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 10, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.user_text = QtWidgets.QLineEdit(self.centralwidget)
        self.user_text.setGeometry(QtCore.QRect(30, 120, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.user_text.setFont(font)
        self.user_text.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.user_text.setText("")
        self.user_text.setMaxLength(10)
        self.user_text.setObjectName("user_text")
        self.pass_text = QtWidgets.QLineEdit(self.centralwidget)
        self.pass_text.setGeometry(QtCore.QRect(30, 220, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.pass_text.setFont(font)
        self.pass_text.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pass_text.setText("")
        self.pass_text.setMaxLength(20)
        self.pass_text.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pass_text.setObjectName("pass_text")
        self.registrar_btn = QtWidgets.QPushButton(self.centralwidget)
        self.registrar_btn.setGeometry(QtCore.QRect(40, 310, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.registrar_btn.setFont(font)
        self.registrar_btn.setObjectName("registrar_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 259, 21))
        self.menubar.setObjectName("menubar")
        self.menuBBDD = QtWidgets.QMenu(self.menubar)
        self.menuBBDD.setObjectName("menuBBDD")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionConectar = QtWidgets.QAction(MainWindow)
        self.actionConectar.setObjectName("actionConectar")
        self.actionSalir = QtWidgets.QAction(MainWindow)
        self.actionSalir.setObjectName("actionSalir")
        self.menuBBDD.addAction(self.actionConectar)
        self.menuBBDD.addSeparator()
        self.menuBBDD.addAction(self.actionSalir)
        self.menubar.addAction(self.menuBBDD.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionConectar.triggered.connect(lambda: conectar_bbdd(self.centralwidget))
        self.actionSalir.triggered.connect(lambda: salir(self.centralwidget))
        self.registrar_btn.clicked.connect(lambda: crear_user(self.centralwidget, self.user_text, self.pass_text))
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Sign up"))
        self.label_2.setText(_translate("MainWindow", "New username:"))
        self.label_3.setText(_translate("MainWindow", "New password:"))
        self.registrar_btn.setText(_translate("MainWindow", "Create"))
        self.menuBBDD.setTitle(_translate("MainWindow", "BBDD"))
        self.actionConectar.setText(_translate("MainWindow", "Conectar"))
        self.actionSalir.setText(_translate("MainWindow", "Salir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
