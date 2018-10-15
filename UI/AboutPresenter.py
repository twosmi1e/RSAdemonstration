# coding=utf-8
# Environment: Python3.7
# Requirement: PyQt5
# Author: Twosmi1e
# Date: 2018.10.06

from UI import AboutUI
from PyQt5.QtWidgets import QWidget

class AboutPresenter(QWidget, AboutUI.Ui_Form_about):
    def __init__(self):
        super(AboutPresenter, self).__init__()

        self.setupUi(self)
