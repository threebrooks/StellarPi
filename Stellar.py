from tkinter import *
import time
import numpy as np
import io
from datetime import datetime, timedelta
from PIL import Image
import subprocess

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

def MainScreenClick(e):
    pixel = maskPic.getpixel((e.x,e.y))
    if (pixel == (255,0,0,255)):
        filename = datetime.now().strftime("%Y%m%d-%H%M%S.jpg")
        if (is_rpi):
            camera.capture(filename)
        sys.exit(0)

is_rpi = IsRaspberryPi()

root = Tk()
root.title("Pi Camera")
root.overrideredirect(True)
dims = (800, 480)
root.geometry('%dx%d+0+0' % dims)
root.configure(background='grey')

mainPic=PhotoImage(file="MainScreen.png")
maskPic=Image.open("MaskScreen.png")

canvas = Canvas(root, width=dims[0], height=dims[1], highlightthickness=0, bg='black')
canvas.bind("<Button-1>", MainScreenClick)
canvas.pack(expand=YES, fill=BOTH)

canvas.create_image(0,0,image=mainPic, anchor=NW)
#root.pack(fill="both", expand=True)

if (is_rpi):
    camera = SetupCamera()

root.mainloop()

