import pyautogui as p
import cv2
from matplotlib import pyplot as plt
import numpy as np
import time
import mss

time.sleep(1)    #Waits for a second
while(100):
    
    with mss.mss() as sct:
            monitor = {"top": 430, "left": 670, "width": 300, "height": 40}  #Defines the region of tiles
            img=sct.grab(monitor) # Captures The Region
    img=np.array(img)
    fimg=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converts it into grayscale
    threshold_level = 10 #defines the threshold of the darkness
    coords = np.column_stack(np.where(fimg < threshold_level))
    if(len(coords)>0):
        print(coords[0][1]) # Prints the coords
        p.click(650+coords[0][1]+30,410+coords[0][0]+90) # Clicks the tiles


# left = 650 top=310 width: 330 height: 40