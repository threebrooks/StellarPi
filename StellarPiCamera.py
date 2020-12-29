from PyQt5 import QtWidgets, uic, QtCore
import time
import sys
import io
from datetime import datetime, timedelta
import subprocess
import StellarPiUI

class StellarPiCamera:
    def __init__(self, is_rpi):
        self.camera = None
        if (is_rpi):
            import picamera
            self.camera = picamera.PiCamera()
            self.camera.resolution = self.camera.MAX_RESOLUTION
            self.camera_preview_fullscreen = False
        self.activate_preview()

    def activate_preview(self):
        if (self.camera):
            preview = self.camera.start_preview()

    def deactivate_preview(self):
        if (self.camera):
            preview = self.camera.stop_preview()

    def take_picture(self):
        if (self.camera):
            filename = datetime.now().strftime("%Y%m%d-%H%M%S.jpg")
            self.camera.capture(filename)
        else:
            filename = "dummy_pic.jpg"
        return filename
    
