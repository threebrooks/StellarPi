from tkinter import *
import time
import picamera
import RPi.GPIO as GPIO  
import numpy as np
import io
from datetime import datetime, timedelta
from PIL import Image

   
root = Tk()
root.title("Pi Camera")
root.overrideredirect(True)
root.geometry('%dx%d+0+0' % (root.winfo_screenwidth(), root.winfo_screenheight()))

def touchEvent(event):
    print(str(event.x)+" "+str(event.y))
    pass

canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight())
canvas.bind("<Button-1>", touchEvent)
canvas.pack()

camera = picamera.PiCamera()
camera_preview_fullscreen = False
camera.start_preview()
 
img = Image.open('ShowOverlay.png')
pad = Image.new('RGB', (
     ((img.size[0] + 31) // 32) * 32,
     ((img.size[1] + 15) // 16) * 16,
     ))
pad.paste(img, (0, 0))
o = camera.add_overlay(pad.tobytes())
o.alpha = 128
o.layer = 3

root.mainloop()

