# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cikti.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgCikti(object):
    def setupUi(self, dlgCikti):
        dlgCikti.setObjectName("dlgCikti")
        dlgCikti.resize(820, 390)
        self.verticalLayout = QtWidgets.QVBoxLayout(dlgCikti)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblKomut = QtWidgets.QLabel(dlgCikti)
        self.lblKomut.setObjectName("lblKomut")
        self.verticalLayout.addWidget(self.lblKomut)
        self.textCikti = QtWidgets.QTextEdit(dlgCikti)
        font = QtGui.QFont()
        font.setFamily("Courier")
        font.setPointSize(10)
        self.textCikti.setFont(font)
        self.textCikti.setObjectName("textCikti")
        self.verticalLayout.addWidget(self.textCikti)

        self.retranslateUi(dlgCikti)
        QtCore.QMetaObject.connectSlotsByName(dlgCikti)

    def retranslateUi(self, dlgCikti):
        _translate = QtCore.QCoreApplication.translate
        dlgCikti.setWindowTitle(_translate("dlgCikti", "Dialog"))
        self.lblKomut.setText(_translate("dlgCikti", "TextLabel"))

