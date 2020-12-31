from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtGui import QPixmap, QIcon
import sys
import os

class StellarPiUI(QtWidgets.QMainWindow):
    def __init__(self, callbacks, camera):
        self.camera = camera
        self.app = QtWidgets.QApplication(sys.argv) 
        super(StellarPiUI, self).__init__() # Call the inherited classes __init__ method
        self.callbacks = callbacks
        uic.loadUi(os.path.join(os.path.dirname(os.path.realpath(__file__)),'StellarPi.ui'), self) # Load the .ui file
        self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.findChild(QtCore.QObject, 'cameraButton').clicked.connect(callbacks['CameraButton_Clicked']) 
        self.findChild(QtCore.QObject, 'exitButton').clicked.connect(callbacks['ExitButton_Clicked']) 
        self.findChild(QtCore.QObject, 'shutterSpeedUpButton').clicked.connect(callbacks['ShutterSpeedUpButton_Clicked']) 
        self.findChild(QtCore.QObject, 'shutterSpeedDownButton').clicked.connect(callbacks['ShutterSpeedDownButton_Clicked']) 
        self.findChild(QtCore.QObject, 'isoUpButton').clicked.connect(callbacks['ISOUpButton_Clicked']) 
        self.findChild(QtCore.QObject, 'isoDownButton').clicked.connect(callbacks['ISODownButton_Clicked']) 
        self.setWindowState(QtCore.Qt.WindowMaximized)
        self.show() 

    def run(self):
        self.app.exec_() 

    def setCameraButtonHot(self, hot):
        if (hot):
            self.findChild(QtCore.QObject, 'cameraButton').setIcon(QIcon(QPixmap("shutter_button_hot.png")))
        else:
            self.findChild(QtCore.QObject, 'cameraButton').setIcon(QIcon(QPixmap("shutter_button.png")))


    def showPicture(self, fname):
        pictureDisplay = self.findChild(QtCore.QObject, 'pictureDisplay') 
        w = pictureDisplay.width()
        h = pictureDisplay.height()
        pixmap = QPixmap(fname)
        pictureDisplay.setPixmap(pixmap.scaled(w,h,QtCore.Qt.KeepAspectRatio))

    def updateElements(self):
        self.findChild(QtCore.QObject, 'shutterSpeedLabel').setText("Shutter\n "+str(self.camera.camera.shutter_speed)+"us") 
        self.findChild(QtCore.QObject, 'isoLabel').setText("ISO\n"+str(self.camera.camera.iso)) 


