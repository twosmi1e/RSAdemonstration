# coding=utf-8
# Environment: Python3.7
# Requirement: PyQt5
# Author: Twosmi1e
# Date: 2018.10.06

from UI import RSAMainUI, DivisionAlgorithmPresenter, AboutPresenter
from PyQt5.QtWidgets import QMainWindow
from random import randint
import math

e = 17
M = 31631
fn = 0
class MainPresenter(QMainWindow, RSAMainUI.Ui_MainWindow):
    def __init__(self):
        super(MainPresenter, self).__init__()

        self.setupUi(self)
        self.DA_ui = DivisionAlgorithmPresenter.DivisionAlgorithmPresenter()
        self.about_ui = AboutPresenter.AboutPresenter()
        self.pushButton.clicked.connect(self.initRSAUI)
        self.actiona_DA.triggered.connect(self.slot_DA)
        self.actiona_about.triggered.connect(self.slot_about)

    def slot_DA(self):
        self.DA_ui.show()

    def slot_about(self):
        self.about_ui.show()

    def initRSAUI(self):
        # 使用全局变量 方便子界面获取值
        global M
        global e
        global fn

        (p, q) = self.genrandom()
        (n, fn) = self.computeN(p, q)
        # 判断φ(n),e是否互质
        while not (self.gcd(fn, e) == 1):
            (p, q) = self.genrandom()
            (n, fn) = self.computeN(p, q)

        self.lineEdit_p.setText(str(p))
        self.lineEdit_q.setText(str(q))
        self.lineEdit_n.setText(str(n))
        self.lineEdit_fn.setText(str(fn))
        self.lineEdit_e.setText(str(e))
        d = self.computeD(fn, e)
        d = round(d)
        self.lineEdit_d.setText(str(d))
        self.lineEdit_M.setText(str(M))
        C = self.encryption(M, e, n)
        self.lineEdit_C.setText(str(C))
        M2 = self.decryption(C, d, n)
        self.lineEdit_M2.setText(str(M2))


    def genrandom(self):
        # 随机生成p,q
        p = randint(1000, 99999)
        q = randint(1000, 99999)
        while not (self.IsPrime(p) and self.IsPrime(q)):
            p = randint(1000, 99999)
            q = randint(1000, 99999)
        return (p, q)

    def computeN(self, p, q):
        n = p * q
        fn = (p-1) * (q-1)
        return (n, fn)
    # 判断是否为素数(因子检测法)
    def IsPrime(self, candidate):
        if ((candidate & 1) == 0):  # 是偶数，除了2，其他偶数全部不是质数
            return candidate == 2
        limit = int(math.sqrt(candidate))
        for i in range(3, limit + 1, 2):
            if candidate % i == 0:
                return False
        return True

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    # 扩展欧几里得算法
    def extendedGCD(self, a, b):
        # a*xi + b*yi = ri
        if b == 0:
            return (1, 0, a)
        # a*x1 + b*y1 = a
        x1 = 1
        y1 = 0
        # a*x2 + b*y2 = b
        x2 = 0
        y2 = 1
        while b != 0:
            # a = b * q + r
            q = math.trunc(a / b)
            # ri = r(i-2) % r(i-1)
            r = a % b
            a = b
            b = r
            # xi = x(i-2) - q*x(i-1)
            x = x1 - q * x2
            x1 = x2
            x2 = x
            # yi = y(i-2) - q*y(i-1)
            y = y1 - q * y2
            y1 = y2
            y2 = y
        return (x1, y1, a)

    def computeD(self, fn, e):
        (x, y, r) = self.extendedGCD(fn, e)
        # y maybe < 0, so convert it
        if y < 0:
            return fn + y
        return y

    def fastExpMod(self, b, e, m):
        """
        e = e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n)

        b^e = b^(e0*(2^0) + e1*(2^1) + e2*(2^2) + ... + en * (2^n))
            = b^(e0*(2^0)) * b^(e1*(2^1)) * b^(e2*(2^2)) * ... * b^(en*(2^n))

        b^e mod m = ((b^(e0*(2^0)) mod m) * (b^(e1*(2^1)) mod m) * (b^(e2*(2^2)) mod m) * ... * (b^(en*(2^n)) mod m) mod m
        """
        result = 1
        while e != 0:
            if (e & 1) == 1:
                # ei = 1, then mul
                result = (result * b) % m
            e >>= 1
            # b, b^2, b^4, b^8, ... , b^(2^n)
            b = (b * b) % m
        return result

    def encryption(self, M, e, n):
        # RSA C = M^e mod n
        return self.fastExpMod(M, e, n)

    def decryption(self, C, d, n):
        # RSA M = C^d mod n
        return self.fastExpMod(C, d, n)
