# coding=utf-8
# Environment: Python3.7
# Requirement: PyQt5
# Author: Twosmi1e
# Date: 2018.10.06

from UI import DivisionAlgorithmUI, MainPresenter
from PyQt5.QtWidgets import QWidget, QTableWidgetItem




class DivisionAlgorithmPresenter(QWidget, DivisionAlgorithmUI.Ui_Form_Divisonalgorithm):
    def __init__(self):

        super(DivisionAlgorithmPresenter, self).__init__()

        self.setupUi(self)
        self.pushButton.clicked.connect(self.inittable)


    def inittable(self):
        self.tableWidget.clear()
        e = MainPresenter.e
        fn = MainPresenter.fn
        self.label_a.setText(str(fn))
        self.label_b.setText(str(e))
        self.tableWidget.setColumnCount(5)
        # self.tableWidget.setRowCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['a', 'b', 'gcd(a, b)', 'x', 'y'])
        a = fn
        b = e

        i = 0
        while(1):
            if not (a == 1 or b == 1):
                self.tableWidget.insertRow(i)
                data_a = QTableWidgetItem(str(a))
                data_b = QTableWidgetItem(str(b))
                gcd = self.gcd(a, b)
                data_gcd = QTableWidgetItem(str(gcd))
                self.tableWidget.setItem(i, 0, data_a)
                self.tableWidget.setItem(i, 1, data_b)
                self.tableWidget.setItem(i, 2, data_gcd)
                (a, b) = self.eachdivide(a, b)
                i = i + 1
            if (b == 1):
                self.tableWidget.insertRow(i)
                data_a = QTableWidgetItem(str(a))
                data_b = QTableWidgetItem(str(b))
                gcd = self.gcd(a, b)
                data_gcd = QTableWidgetItem(str(gcd))
                self.tableWidget.setItem(i, 0, data_a)
                self.tableWidget.setItem(i, 1, data_b)
                self.tableWidget.setItem(i, 2, data_gcd)
                x = 0
                y = int((1 - a * x) / b)
                data_x = QTableWidgetItem(str(x))
                data_y = QTableWidgetItem(str(y))
                self.tableWidget.setItem(i, 3, data_x)
                self.tableWidget.setItem(i, 4, data_y)
                j = i
                while not i == 0:
                    j = j + 1
                    i = i - 1
                    self.tableWidget.insertRow(j)
                    a = self.tableWidget.item(i, 0).text()
                    b = self.tableWidget.item(i, 1).text()
                    gcd = self.gcd(int(a), int(b))
                    data_a = QTableWidgetItem(str(a))
                    data_b = QTableWidgetItem(str(b))
                    data_gcd = QTableWidgetItem(str(gcd))
                    self.tableWidget.setItem(j, 0, data_a)
                    self.tableWidget.setItem(j, 1, data_b)
                    self.tableWidget.setItem(j, 2, data_gcd)
                    # print(a)
                    # print(b)
                    # print(x, y)
                    (x, y) = self.gcdgetxy(int(a), int(b), y)
                    data_x = QTableWidgetItem(str(x))
                    data_y = QTableWidgetItem(str(y))
                    self.tableWidget.setItem(j, 3, data_x)
                    self.tableWidget.setItem(j, 4, data_y)
                break

    def gcdgetxy(self, a, b, y):
        x = y
        y = int((1 - a * x) / b)
        return (x, y)



    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    # 辗转相除
    def eachdivide(self, a, b):
        if a > b:
            if ((a % b) > b):
                return (a % b, b)
            else:
                return (b, a % b)
        else:
            if ((b % a) > a):
                return (b % a, a)
            else:
                return (a, b % a)





