# coding=utf-8
# Environment: Python3.7
# Requirement: PyQt5
# Author: Twosmi1e
# Date: 2018.10.06




import sys
from UI import MainPresenter
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_presenter = MainPresenter.MainPresenter()
    main_presenter.show()
    sys.exit(app.exec())