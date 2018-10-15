# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DivisionAlgorithmUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_Divisonalgorithm(object):
    def setupUi(self, Form_Divisonalgorithm):
        Form_Divisonalgorithm.setObjectName("Form_Divisonalgorithm")
        Form_Divisonalgorithm.resize(617, 374)
        self.label = QtWidgets.QLabel(Form_Divisonalgorithm)
        self.label.setGeometry(QtCore.QRect(30, 20, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form_Divisonalgorithm)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 59, 231, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label_a = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_a.setObjectName("label_a")
        self.horizontalLayout.addWidget(self.label_a)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.label_b = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_b.setObjectName("label_b")
        self.horizontalLayout_2.addWidget(self.label_b)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(Form_Divisonalgorithm)
        self.tableWidget.setGeometry(QtCore.QRect(10, 180, 601, 181))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(Form_Divisonalgorithm)
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 81, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form_Divisonalgorithm)
        QtCore.QMetaObject.connectSlotsByName(Form_Divisonalgorithm)

    def retranslateUi(self, Form_Divisonalgorithm):
        _translate = QtCore.QCoreApplication.translate
        Form_Divisonalgorithm.setWindowTitle(_translate("Form_Divisonalgorithm", "辗转相除演示"))
        self.label.setText(_translate("Form_Divisonalgorithm", "ax+by=gcd(a,b)"))
        self.label_3.setText(_translate("Form_Divisonalgorithm", "a=φ(n)="))
        self.label_a.setText(_translate("Form_Divisonalgorithm", "TextLabel"))
        self.label_4.setText(_translate("Form_Divisonalgorithm", "b=e="))
        self.label_b.setText(_translate("Form_Divisonalgorithm", "TextLabel"))
        self.pushButton.setText(_translate("Form_Divisonalgorithm", "StepMode"))

