import sys
from PySide2 import QtWidgets, QtGui, QtCore
from view.main_window import MainWindow
import mysql.connector

class App(QtWidgets.QApplication):
    def __init__(self):
        super().__init__(sys.argv)

    def start(self):
        main_window = MainWindow()
        main_window.show()
    
