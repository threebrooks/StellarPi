from PyQt5 import QtWidgets, uic, QtCore
import time
import sys
import io
from datetime import datetime, timedelta
import subprocess
import StellarPiUI, StellarPiCamera

class StellarPi:
    def __init__(self):
        self.camera = StellarPiCamera.StellarPiCamera(self.IsRaspberryPi())
        callbacks = {
            'CameraButton_Clicked': self.CameraButton_Clicked
        }
        self.ui = StellarPiUI.StellarPiUI(callbacks) 

    def IsRaspberryPi(self):
      os_id = subprocess.Popen("cat /etc/os-release | grep \"^ID=\"", shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8').rstrip()
      return (os_id == "ID=raspbian")
    
    def CameraButton_Clicked(self,e):
        fname = self.camera.take_picture()
        self.camera.deactivate_preview()
        self.ui.show_picture(fname)
    
    def run(self):
        self.ui.run()

StellarPi().run()

