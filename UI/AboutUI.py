# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_about(object):
    def setupUi(self, Form_about):
        Form_about.setObjectName("Form_about")
        Form_about.resize(400, 146)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form_about)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(50, 30, 261, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(Form_about)
        QtCore.QMetaObject.connectSlotsByName(Form_about)

    def retranslateUi(self, Form_about):
        _translate = QtCore.QCoreApplication.translate
        Form_about.setWindowTitle(_translate("Form_about", "关于"))
        self.label.setText(_translate("Form_about", "RSA加密解密演示程序"))
        self.label_2.setText(_translate("Form_about", "code by twosmi1e 18.10.6"))

