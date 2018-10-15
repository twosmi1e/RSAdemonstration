# coding=utf-8
# Environment: Python3.7
# Requirement: PyQt5
# Author: Twosmi1e
# Date: 2018.10.06

from UI import DivisionAlgorithmUI, MainPresenter
from PyQt5.QtWidgets import QWidget, QTableWidgetItem
from PyQt5.Qt import QColor
from random import randint




class DivisionAlgorithmPresenter(QWidget, DivisionAlgorithmUI.Ui_Form_Divisonalgorithm):
    def __init__(self):

        super(DivisionAlgorithmPresenter, self).__init__()

        self.setupUi(self)
        self.pushButton.clicked.connect(self.initDAUI)

    # 初始化表格并填充数据
    def initDAUI(self):
        # 行数清零，清除内容
        self.tableWidget.setRowCount(0)
        self.tableWidget.clear()
        # 获取主界面的e,fn值
        e = MainPresenter.e
        fn = MainPresenter.fn

        self.label_a.setText(str(fn))
        self.label_b.setText(str(e))
        self.tableWidget.setColumnCount(5)
        # 修改为动态插入行
        # self.tableWidget.setRowCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['a', 'b', 'gcd(a, b)', 'x', 'y'])
        a = fn
        b = e
        (R, G ,B) = (255, 255, 255)
        bgcolor_b = QColor(R, G, B)
        i = 0
        while(1):
            # 填充辗转相除部分的数据
            if not (a == 1 or b == 1):
                self.tableWidget.insertRow(i)
                data_a = QTableWidgetItem(str(a))
                data_b = QTableWidgetItem(str(b))
                gcd = self.gcd(a, b)
                data_gcd = QTableWidgetItem(str(gcd))
                bgcolor_a = bgcolor_b
                (R, G, B) = self.randcolor(R, G, B)
                bgcolor_b = QColor(R, G, B)
                data_a.setBackground(bgcolor_a)
                data_b.setBackground(bgcolor_b)
                self.tableWidget.setItem(i, 0, data_a)
                self.tableWidget.setItem(i, 1, data_b)
                self.tableWidget.setItem(i, 2, data_gcd)
                (a, b) = self.eachdivide(a, b)
                i = i + 1
            # 填充后半部分的数据
            if (b == 1):
                self.tableWidget.insertRow(i)
                data_a = QTableWidgetItem(str(a))
                data_b = QTableWidgetItem(str(b))
                gcd = self.gcd(a, b)
                data_gcd = QTableWidgetItem(str(gcd))
                data_a.setBackground(bgcolor_b)
                self.tableWidget.setItem(i, 0, data_a)
                self.tableWidget.setItem(i, 1, data_b)
                self.tableWidget.setItem(i, 2, data_gcd)
                x = 0
                y = int((1 - a * x) / b)
                data_x = QTableWidgetItem(str(x))
                data_y = QTableWidgetItem(str(y))
                (R, G, B) = self.randcolor(R, G, B)
                bgcolor_y = QColor(R, G, B)
                data_y.setBackground(bgcolor_y)
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
                    bgcolor_x = bgcolor_y
                    (R, G, B) = self.randcolor(R, G, B)
                    bgcolor_y = QColor(R, G, B)
                    data_x.setBackground(bgcolor_x)
                    data_y.setBackground(bgcolor_y)
                    self.tableWidget.setItem(j, 3, data_x)
                    self.tableWidget.setItem(j, 4, data_y)
                break
        # 如果最后模数为负，则取正
        result_d = self.tableWidget.item(j, 4).text()
        if (int(result_d) < 0):
            d = int(result_d) + fn
            data_d = QTableWidgetItem(str(d))
            self.tableWidget.setItem(j, 4, data_d)

    # 随机生成颜色
    def randcolor(self, r, g, b):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)

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





