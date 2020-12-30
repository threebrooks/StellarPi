from PyQt5 import QtWidgets, uic, QtCore
import time
import sys
import io
from datetime import datetime, timedelta
import subprocess
import StellarPiUI, StellarPiCamera
from enum import Enum

class Mode(Enum):
    ShowPicture = 1
    ShowPreview = 2

class StellarPi:
    def __init__(self):
        self.mode = Mode.ShowPreview
        self.camera = StellarPiCamera.StellarPiCamera(self.IsRaspberryPi())
        callbacks = {
            'CameraButton_Clicked': self.CameraButton_Clicked,
            'ExitButton_Clicked': self.ExitButton_Clicked
        }
        self.ui = StellarPiUI.StellarPiUI(callbacks) 

    def IsRaspberryPi(self):
      os_id = subprocess.Popen("cat /etc/os-release | grep \"^ID=\"", shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8').rstrip()
      return (os_id == "ID=raspbian")
    
    def CameraButton_Clicked(self,e):
        if (self.mode == Mode.ShowPreview):
            fname = self.camera.take_picture()
            self.camera.deactivate_preview()
            self.ui.show_picture(fname)
            self.mode = Mode.ShowPicture
        else:
            self.camera.activate_preview()
            self.mode = Mode.ShowPreview
    
    def ExitButton_Clicked(self,e):
        sys.exit(0)

    def run(self):
        self.ui.run()

StellarPi().run()

