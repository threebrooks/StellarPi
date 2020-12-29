from PyQt5 import QtWidgets, uic, QtCore
import sys

class StellarPiUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(StellarPiUI, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('/mnt/c/Users/Me/Desktop/StellarPi.ui', self) # Load the .ui file
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show() # Show the GUI


