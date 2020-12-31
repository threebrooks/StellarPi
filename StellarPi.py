from PyQt5 import QtWidgets, uic, QtCore
import time
import sys
import io
from datetime import datetime, timedelta
import subprocess
import StellarPiUI, StellarPiCamera
from enum import Enum
import threading

class Mode(Enum):
    ShowPreview = 1
    DelayTakePicture = 2
    ShowPicture = 3

class StellarPi:
    def __init__(self):
        self.mode = Mode.ShowPreview
        self.camera = StellarPiCamera.StellarPiCamera(self.IsRaspberryPi())
        self.camera.setPreview(True)
        callbacks = {
            'CameraButton_Clicked': self.CameraButton_Clicked,
            'ExitButton_Clicked': self.ExitButton_Clicked,
            'ShutterSpeedUpButton_Clicked': self.ShutterSpeedUpButton_Clicked,
            'ShutterSpeedDownButton_Clicked': self.ShutterSpeedDownButton_Clicked,
            'ISODownButton_Clicked': self.ISODownButton_Clicked,
            'ISOUpButton_Clicked': self.ISOUpButton_Clicked,
        }
        self.ui = StellarPiUI.StellarPiUI(callbacks, self.camera) 
        self.ui.updateElements()

    def IsRaspberryPi(self):
      os_id = subprocess.Popen("cat /etc/os-release | grep \"^ID=\"", shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8').rstrip()
      return (os_id == "ID=raspbian")

    def DelayedTakePicture(self):
        for i in range(5):
            self.ui.setCameraButtonHot(i % 2 == 1)
            time.sleep(1)
        fname = self.camera.takePicture()
        self.camera.setPreview(False)
        self.ui.showPicture(fname)
        self.mode = Mode.ShowPicture
    
    def CameraButton_Clicked(self,e):
        if (self.mode == Mode.DelayTakePicture):
            return
        elif (self.mode == Mode.ShowPreview):
            threading.Thread(target=self.DelayedTakePicture).start()
        else:
            self.camera.setPreview(True)
            self.mode = Mode.ShowPreview
    
    def ExitButton_Clicked(self,e):
        sys.exit(0)

    def ShutterSpeedUpButton_Clicked(self):
        self.camera.setShutterSpeed(True)
        self.ui.updateElements()

    def ShutterSpeedDownButton_Clicked(self):
        self.camera.setShutterSpeed(False)
        self.ui.updateElements()

    def ISOUpButton_Clicked(self):
        self.camera.setISO(True)
        self.ui.updateElements()

    def ISODownButton_Clicked(self):
        self.camera.setISO(False)
        self.ui.updateElements()

    def run(self):
        self.ui.run()

StellarPi().run()

