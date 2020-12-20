from tkinter import *
import time
import numpy as np
import io
from datetime import datetime, timedelta
from PIL import Image

def SetupCamera():
    import picamera
    camera = picamera.PiCamera()
    camera.resolution = camera.MAX_RESOLUTION
    camera_preview_fullscreen = False
    preview = camera.start_preview()

def PicButtonClick():
    filename = datetime.now().strftime("%Y%m%d-%H%M%S.jpg")
    camera.capture(filename)

root = Tk()
root.title("Pi Camera")
root.overrideredirect(True)
root.geometry('%dx%d+0+0' % (root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background='black')
root.wm_attributes('-alpha', 0.7)  

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=5)
root.columnconfigure(2, weight=1)

shutterPic=PhotoImage(file="Shutter.png")
picButton = Button(root, command=PicButtonClick, image=shutterPic)
picButton.grid(row=1, column=3)

SetupCamera()

root.mainloop()

