#!/usr/bin/python3

"""
Written by Albert"Anferensis"Ong

Created: 2023.08.24
"""

import sys
from PyQt5.QtWidgets import QApplication
from main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    sys.exit(app.exec_())
  
if __name__ == "__main__": 
    main()  