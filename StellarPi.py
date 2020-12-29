from PyQt5 import QtWidgets, uic, QtCore
import time
import sys
import io
from datetime import datetime, timedelta
import subprocess
import StellarPiUI

def IsRaspberryPi():
  os_id = subprocess.Popen("cat /etc/os-release | grep \"^ID=\"", shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8').rstrip()
  return (os_id == "ID=raspbian")

def SetupCamera():
    import picamera
    camera = picamera.PiCamera()
    camera.resolution = camera.MAX_RESOLUTION
    camera_preview_fullscreen = False
    preview = camera.start_preview()
    return camera

def CameraButtClick(e):
    filename = datetime.now().strftime("%Y%m%d-%H%M%S.jpg")
    if (is_rpi):
        camera.capture(filename)
    sys.exit(0)

is_rpi = IsRaspberryPi()

if (is_rpi):
    camera = SetupCamera()

app = QtWidgets.QApplication(sys.argv) 
window = StellarPiUI.StellarPiUI() 
app.exec_() 


