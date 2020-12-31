from PyQt5 import QtWidgets, uic, QtCore
import time
import sys
import io
import os
from datetime import datetime, timedelta
import subprocess
import StellarPiUI

class DummyCamera:
    def __init__(self):
        self.shutter_speed = 100
        self.iso = 400
        pass

    def capture(self, fname):
        pass

    def start_preview(self):
        pass

    def stop_preview(self):
        pass

class StellarPiCamera:
    def __init__(self, is_rpi):
        self.camera = None
        if (is_rpi):
            import picamera
            self.camera = picamera.PiCamera()
            self.camera.resolution = self.camera.MAX_RESOLUTION
        else:
            self.camera = DummyCamera()
        self.camera.awb_mode = 'off'
#        self.camera.brightness = 50
#        self.camera.shutter_speed = 100
        self.camera.exposure_mode = 'night' 
        self.camera.image_denoise = True 
#        self.camera.iso = 400
#        self.camera_preview_fullscreen = False

    def setPreview(self, on):
        if (on):
            preview = self.camera.start_preview()
        else:
            preview = self.camera.stop_preview()

    def takePicture(self):
        if (type(self.camera) == DummyCamera):
            filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dummy_pic.jpg")
        else:
            filename = "/var/www/html/"+datetime.now().strftime("%Y%m%d-%H%M%S.jpg")
        self.camera.capture(filename)
        return filename

    def setShutterSpeed(self, up):
        speed = self.camera.shutter_speed
        if (up):
            speed = int(speed*2)
        else:
            speed = int(speed/2)
        speed = max(min(1000000,speed),1)
        self.camera.shutter_speed = speed
        return speed

    def setBrightness(self, up):
        brightness = self.camera.brightness 
        if (up):
            brightness += 1
        else:
            brightness -= 1
        brightness = max(min(100,brightness),0)
        self.camera.brightness = brightness
        return brightness

    def setISO(self, up):
        iso = self.camera.iso
        if (up):
            iso += 100
        else:
            iso -= 100
        iso = max(min(1600,iso),100)
        self.camera.iso = iso
        return iso


    
