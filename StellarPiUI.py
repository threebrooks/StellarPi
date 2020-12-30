from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPixmap
import sys

class StellarPiUI(QtWidgets.QMainWindow):
    def __init__(self, callbacks):
        self.app = QtWidgets.QApplication(sys.argv) 
        super(StellarPiUI, self).__init__() # Call the inherited classes __init__ method
        self.callbacks = callbacks
        uic.loadUi('StellarPi.ui', self) # Load the .ui file
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.findChild(QtCore.QObject, 'cameraButton').clicked.connect(callbacks['CameraButton_Clicked']) 
        self.findChild(QtCore.QObject, 'exitButton').clicked.connect(callbacks['ExitButton_Clicked']) 
        self.show() 

    def run(self):
        self.app.exec_() 

    def show_picture(self, fname):
        pictureDisplay = self.findChild(QtCore.QObject, 'pictureDisplay') 
        w = pictureDisplay.width()
        h = pictureDisplay.height()
        pixmap = QPixmap(fname)
        pictureDisplay.setPixmap(pixmap.scaled(w,h,QtCore.Qt.KeepAspectRatio))
        #pictureDisplay.setMask(pixmap.mask())


