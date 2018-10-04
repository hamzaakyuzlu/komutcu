# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ana.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgAna(object):
    def setupUi(self, dlgAna):
        dlgAna.setObjectName("dlgAna")
        dlgAna.resize(709, 45)
        self.horizontalLayout = QtWidgets.QHBoxLayout(dlgAna)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblKomut = QtWidgets.QLabel(dlgAna)
        self.lblKomut.setObjectName("lblKomut")
        self.horizontalLayout.addWidget(self.lblKomut)
        self.editKomut = QtWidgets.QLineEdit(dlgAna)
        self.editKomut.setObjectName("editKomut")
        self.horizontalLayout.addWidget(self.editKomut)
        self.btnKomut = QtWidgets.QPushButton(dlgAna)
        self.btnKomut.setObjectName("btnKomut")
        self.horizontalLayout.addWidget(self.btnKomut)

        self.retranslateUi(dlgAna)
        self.editKomut.returnPressed.connect(dlgAna.calistir)
        self.btnKomut.clicked.connect(dlgAna.calistir)
        QtCore.QMetaObject.connectSlotsByName(dlgAna)

    def retranslateUi(self, dlgAna):
        _translate = QtCore.QCoreApplication.translate
        dlgAna.setWindowTitle(_translate("dlgAna", "Dialog"))
        self.lblKomut.setText(_translate("dlgAna", "Komut"))
        self.btnKomut.setText(_translate("dlgAna", "Calistir"))

